'''
Created on 05/06/2014

@author: ASUS
'''
from psa.util import argmax


class PDM:
    
    
    def utilidade(self, modelo, epsilon): #modeloPDM class ModeloPDM, epsilon : float
        # alegroritmo da p. 14 dos slides pds_1
        S, A, gama = modelo.S, modelo.A, modelo.gama() #isto e um metodo..... agora posso chamar S()
        # se fizer gama = modelo.gama(),  como gama e uma ctt, fico com o valor de invocacao do metodo e n com o metodo em si
        
        Un = dict((s, 0) for s in S()) # CHAVE SaO OS ESTADOS, PK e u(S)
        delta_max = epsilon * (1 - gama) / gama #epsilon e o erro real admissivel maximo
        while True:
            U = Un.copy()
            delta = 0
            for s in S():
                Un[s] = max ( self._util_accao(modelo, s, a, U) 
                              for a in A(s))
                delta = max ( delta, abs(Un[s] - U[s]) ) ## diferenca da utilidade na nova iteracao e na antiga
            if delta <  delta_max:
                break
        return Un
                
    def _util_accao(self, modelo, s, a, U): #estado e acao
        T,R, suc, gama =  modelo.T, modelo.R, modelo.suc, modelo.gama()
        return sum(T(s,a,sn)*(R(s,a,sn)+gama*U[sn])
                   for sn in suc(s,a))
        
    def politica(self, modelo, U):
        #argMax e da psa e recebe o dominio de valores e a funcao, e pega em cada elemento do dominio e activa a funcao com esse elemtno, 
        #calcular os valores todos e retornar o elemento que produziu os valores maiores
        S, A = modelo.S, modelo.A
        pol = {}
        for s in S():
            pol[s] = argmax(A(s), lambda a: self._util_accao(modelo, s, a, U)) 
        return pol