'''
Created on 29/05/2014

@author: ASUS
'''
from src.pee.problema_heuristico import ProblemaHeuristico
from psa.util import dist


class ProblemaRacPee(ProblemaHeuristico):
    
    def __init__(self, pos_agente, capacidades, objetivo):
        self._estado_inicial = pos_agente
        self._tabela_operadores = capacidades
        self._estado_final=objetivo
    
    def heuristica(self, estado):
        return dist(estado , self._estado_final) #distancia ao alvo

    def estado_inicial(self):
        return self._estado_inicial
        #return Estado
        
    def objectivo(self,Estado):
        return Estado == self._estado_final
        #return Boolean
     
    def operadores(self):
        return self._tabela_operadores
        #return Operadors []
         
    
    
    
    #===========================================================================
    # def __init__(self, estado_inicial, estado_final):
    #     self._estado_inicial=estado_inicial
    #     self._estado_final = estado_final
    #     self._tabela_operadores = [MoverPuzzle((-1,0)),MoverPuzzle((1,0)),MoverPuzzle((0,-1)),MoverPuzzle((0,1))]
    # 
    # 
    # def estado_inicial(self):
    #     return self._estado_inicial
    #     #return Estado
    #    
    # def objectivo(self,Estado):
    #     return Estado == self._estado_final
    #     #return Boolean
    # 
    # def operadores(self):
    #     return self._tabela_operadores
    #     #return Operadors []
    #     
    # def heuristica(self, estado):
    #     return puzzle.distmanhattan(estado, self._estado_final)
    #     #return puzzle.numpecasforalugar(estado, self._estado_final)
    #===========================================================================