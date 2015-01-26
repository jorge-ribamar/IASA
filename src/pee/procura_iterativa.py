'''
Created on 16/05/2014

@author: ASUS
'''
from src.pee.procura_profundidade_limitada import ProcuraProfundidadeLimitada

class ProcuraIterativa(ProcuraProfundidadeLimitada):
        
    def procurar(self, Problema, limiteProfundidade, incremento):
        limProcura = 1
        percurso = None
        while (limProcura <= limiteProfundidade):
            percurso = super(ProcuraIterativa, self).procurar( Problema, limProcura) 
            limProcura +=incremento
            if percurso is not None:
                return percurso