'''
Created on 05/06/2014

@author: ASUS
'''
from src.PDM.modelo_pdm import ModeloPDM
# e uma interface
class ModeloRecAlvos(ModeloPDM):
    
    def __init__(self, crencas,capacidades ,intencoes ): #capacidades - operadores
        self._crencas = crencas
        self._capacidades = capacidades
        self._intencoes = intencoes 
        self._gama=0.99
        self._rmax=20
    
    def S(self):
        return self._crencas.posicoes()

    # s e estado, a operador e sn prox estado
    
    def A(self, s):
        return self._capacidades
    
    def T(self, s, a, sn): #e um ambiente determinista
        if s in self._intencoes: #Estado terminal
            return 0.0
        else:
            return 1.0
    
    def R(self, s, a, sn):
        if sn in self._intencoes:
            r = self._rmax
        elif sn == s:
            r = -self._rmax
        else:
            r=0
        return r-a.custo(s,sn)

    def gama(self):
        return self._gama
    
    def suc(self, s,a): #significa sucessor
        #produz s', o novo estado
        sn = a.aplicar(s) # a e um operador, tem o metodo aplicar
        if sn is None:
            return [s] #e uma lista no caso geral
        else: 
            return [sn]