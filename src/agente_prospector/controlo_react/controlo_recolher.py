'''
Created on 28/03/2014

@author: ASUS
'''
from src.agente_prospector.controlo_react.reaccoes.recolher.recolher import Recolher
from agente_prospector.agente.controlo import Controlo


class ControloRecolher(Controlo):
    
    def __init__(self):
        self._reaccao = Recolher()
    
    #Recebe uma percepcao, processa-a e devolve a accao respectiva
    def processar(self, percepcao):
        #Obtem-se a accao que e resposta ao impulso percepcao, mediante a organizacao interna de self._reaccao
        #Internamente sao obtidas as respostas de cada reacao a percepcao e selecionada a mais prioritaria
        accao = self._reaccao.activar(percepcao)
        return accao