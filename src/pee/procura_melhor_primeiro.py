'''
Created on 09/05/2014

@author: rr
'''

from pee.procura_grafo import ProcuraGrafo

class ProcuraMelhorPrimeiro(ProcuraGrafo):
    
    #avalia o custo de um no 
    def avaliacao(self,no):
        return self.f(no)
    
    #serve para ordenar a fronteira de exploracao que determina que nos vao ser expandidos
    def ordem(self,no):
        #ordenar pela funcao f
        return self.f(no)
        
      
    def f(self,no):
        #return float
        raise NotImplementedError