'''
Created on 08/05/2014

@author: ASUS
'''

from src.pee.problema_heuristico import ProblemaHeuristico
from src.testePuzzle.mover_puzzle import MoverPuzzle
import puzzle



class ProblemaPuzzle(ProblemaHeuristico):
    
    def __init__(self, estado_inicial, estado_final):
        self._estado_inicial=estado_inicial
        self._estado_final = estado_final
        self._tabela_operadores = [MoverPuzzle((-1,0)),MoverPuzzle((1,0)),MoverPuzzle((0,-1)),MoverPuzzle((0,1))]
    
    
    def estado_inicial(self):
        return self._estado_inicial
        #return Estado
       
    def objectivo(self,Estado):
        return Estado == self._estado_final
        #return Boolean
    
    def operadores(self):
        return self._tabela_operadores
        #return Operadors []
        
    def heuristica(self, estado):
        return puzzle.distmanhattan(estado, self._estado_final)
        #return puzzle.numpecasforalugar(estado, self._estado_final)
