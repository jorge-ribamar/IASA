'''
Created on 03/04/2014

@author: ASUS
'''
import sys
sys.path.append("..")
from agente_prospector.controlo_react.reaccao.reaccao import Reaccao


class SeguirPotencialDir(Reaccao):
    def __init__(self,passo, direccao):
        self._direccao= direccao
        self._passo = passo
        
    def _detectar_estimulo(self, percepcao):
        potencial = percepcao[self._direccao].pot_alvo
        if potencial>0:
            return potencial
        
    def _gerar_resposta(self, distancia):
        accao = (self._passo, self._direccao)
        return (distancia, accao)
