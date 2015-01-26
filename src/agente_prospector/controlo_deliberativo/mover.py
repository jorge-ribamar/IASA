'''
Created on 23/05/2014

@author: ASUS
'''

from src.pee.operador import Operador
from psa.util import dist, mover

class Mover(Operador):
    
    def __init__(self, crencas, angulo):
        self._crencas = crencas
        self._angulo=angulo
        self.ang= angulo
        #raise NotImplementedError
    
    def aplicar(self, estado):
        pos = mover(estado, self._angulo)
        if self._crencas.pos_valida(pos):
            return pos 
        #raise NotImplementedError
        #return Estado
    
    def custo(self, Estado, Estado_sucessor):
        return dist(Estado, Estado_sucessor)
        #return float
    
    def getAngulo(self):
        return self._angulo
    
        
    