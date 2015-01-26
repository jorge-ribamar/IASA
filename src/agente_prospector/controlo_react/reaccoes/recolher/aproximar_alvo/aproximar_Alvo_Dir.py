'''
Created on 28/03/2014

@author: ASUS
'''
import sys
sys.path.append("..")
from agente_prospector.controlo_react.reaccao.reaccao import Reaccao


class AproximarAlvoDir(Reaccao):
    def __init__(self, direccao):
        self._direccao= direccao
        
    def _detectar_estimulo(self, percepcao):
        if percepcao[self._direccao].alvo:
            return percepcao[self._direccao].distancia
        
    def _gerar_resposta(self, distancia):
        prioridade = 1.0/(1+distancia)
        accao = (1, self._direccao)
        return (prioridade, accao)