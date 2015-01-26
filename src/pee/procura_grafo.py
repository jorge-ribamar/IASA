'''
Created on 02/05/2014

@author: ASUS
'''
from src.pee.procura import Procura

class ProcuraGrafo(Procura):

    
    def expandir_fronteira(self, no):
        no_mem = self._memoria_exp.obter(no)
        if no_mem is None or self.avaliacao(no) < self.avaliacao(no_mem):
            super(ProcuraGrafo,self).expandir_fronteira(no)
       
    def avaliacao(self,no):
        return no._profundidade
        #raise NotImplementedError
        #return float #quanto mais baixo melhor
            