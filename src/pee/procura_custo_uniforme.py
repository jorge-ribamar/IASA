'''
Created on 09/05/2014

@author: rr
'''
from pee.procura_melhor_primeiro import ProcuraMelhorPrimeiro



class ProcuraCustoUniforme(ProcuraMelhorPrimeiro):
    
    
    def f(self,no):
        return no.custo
        
    
    