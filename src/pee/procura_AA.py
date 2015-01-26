'''
Created on 16/05/2014

@author: ASUS
'''
from src.pee.procura_melhor_primeiro import ProcuraMelhorPrimeiro

class Procura_AA(ProcuraMelhorPrimeiro):
    
    def f(self, no):
        return self._problema.heuristica(no._estado) + no.custo
    