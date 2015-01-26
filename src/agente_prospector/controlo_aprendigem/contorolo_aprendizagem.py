'''
Created on 12/06/2014

@author: ASUS
'''


from src.agente_prospector.agente.controlo import Controlo
from src.aprendizagemReforco.mec_aprendizagem_sarsa import MecAprendizagemSARSA

class ControloAprendizagem(Controlo):
    
    def __init__(self):
        self._mec_aprend = MecAprendizagemSARSA()
        
    def processar(self, percepcao):
        raise NotImplementedError #    