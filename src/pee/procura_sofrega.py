'''
Created on 15/05/2014

@author: ASUS
'''

from src.pee.procura_melhor_primeiro import ProcuraMelhorPrimeiro

class ProcuraSofrega(ProcuraMelhorPrimeiro):
    
    def f(self, no):
        return self._problema.heuristica(no._estado)
    
    
    