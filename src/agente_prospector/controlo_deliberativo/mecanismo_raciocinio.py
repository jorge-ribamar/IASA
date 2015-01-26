'''
Created on 23/05/2014

@author: ASUS
'''

class MecanismoRaciocinio:
    #####e uma interface
        
    def planear(self, crencas, capacidades, intencoes):
        raise NotImplementedError
    
    def executar(self, crencas = None):
        # tem as crencas p retirar a posicao do agente
        # crencas = None por omissao pk podem haver execucao em que o plano e sequencial e n depende da pos do agente
        raise NotImplementedError