'''
Created on 24/04/2014

@author: ASUS
'''
from src.pee.operador import Operador

class Transportar(Operador):
    def __init__(self, estado_origem, estado_destino, custo):
        self._estado_origem=estado_origem
        self._estado_destino=estado_destino
        self._custo = custo
        
    def aplicar(self, estado):
        if self._estado_origem == estado:
            return self._estado_destino
        #return estado_sucessor
    
    def custo(self, Estado, Estado_sucessor):
        if Estado==self._estado_origem:
            return self._custo
    