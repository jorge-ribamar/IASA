'''
Created on 16/05/2014

@author: ASUS
'''

from src.pee.procura_profundidade import ProcuraProfundidade


class ProcuraProfundidadeLimitada(ProcuraProfundidade):

    def expandir(self, no):
        if no._profundidade <= self._maxProfundidade:
            super(ProcuraProfundidadeLimitada, self).expandir(no)
            
    def procurar(self, Problema, maxProfundidade):
        self._maxProfundidade = maxProfundidade
        return super(ProcuraProfundidadeLimitada,self).procurar(Problema)
            