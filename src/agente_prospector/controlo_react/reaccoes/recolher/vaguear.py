'''
Created on 28/03/2014

@author: ASUS
'''

import sys
sys.path.append("..")
import random
from psa.actuador import ESQ, DIR, FRT
from agente_prospector.controlo_react.reaccao.reaccao import Reaccao

class Vaguear(Reaccao):
    def _gerar_resposta(self, estimulo):
        return random.choice([(0,ESQ),(0,DIR),(1,FRT)])
    
    def _detectar_estimulo(self, percepcao):
        return True