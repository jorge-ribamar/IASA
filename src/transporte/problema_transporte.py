'''
Created on 24/04/2014

@author: ASUS
'''

from src.pee.problema import Problema
from src.transporte.transportar import Transportar

class ProblemaTransporte(Problema):
    
    def __init__(self, estado_inicial, estado_final, tabela_ligacoes):
        self._estado_inicial=estado_inicial
        self._estado_final = estado_final
        self._tabela_operadores = [Transportar(e_origem, e_destino, preco) for (e_origem,e_destino,preco) in tabela_ligacoes]
    
    def estado_inicial(self):
        return self._estado_inicial
        #return Estado
       
    def objectivo(self,Estado):
        return Estado == self._estado_final
        #return Boolean
    
    def operadores(self):
        return self._tabela_operadores
        #return Operadors []