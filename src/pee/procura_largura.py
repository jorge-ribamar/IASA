'''
Created on 24/04/2014

@author: ASUS
'''
from src.pee.procura_grafo import ProcuraGrafo

class ProcuraLargura(ProcuraGrafo):
    
    def ordem(self, no):
        return no._profundidade
        #return float 