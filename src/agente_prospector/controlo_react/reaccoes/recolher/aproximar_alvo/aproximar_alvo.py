'''
Created on 28/03/2014

@author: ASUS
'''

import sys
sys.path.append("..")
from agente_prospector.controlo_react.reaccao.seleccao import Seleccao
from src.agente_prospector.controlo_react.reaccoes.recolher.aproximar_alvo.aproximar_Alvo_Dir import AproximarAlvoDir
from psa.actuador import ESQ, DIR, FRT

class AproximarAlvo(Seleccao):
    def _definir_reaccoes(self):
        return [AproximarAlvoDir(ESQ), AproximarAlvoDir(DIR), AproximarAlvoDir(FRT)]
    