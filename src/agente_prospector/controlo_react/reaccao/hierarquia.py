'''
Created on 27/03/2014

@author: Portatil
'''
import sys
sys.path.append("..")
from agente_prospector.controlo_react.reaccao.comportamento import Comportamento

class Hierarquia(Comportamento):
        def _seleccionar_accao(self,respostas):
            #devolve a acvao mais prioritaria da lista de respostas de entrada
            return respostas[0]