'''
Created on 28/03/2014

@author: ASUS
'''
import sys

sys.path.append("..")
from src.agente_prospector.controlo_react.reaccoes.recolher.evitar_obstaculo import EvitarObstaculo
from agente_prospector.controlo_react.reaccao.hierarquia import Hierarquia
from src.agente_prospector.controlo_react.reaccoes.recolher.vaguear import Vaguear
from src.agente_prospector.controlo_react.reaccoes.recolher.aproximar_alvo.aproximar_alvo import AproximarAlvo
from src.agente_prospector.controlo_react.reaccoes.recolher.seguir_potencial.seguir_potencial import SeguirPotencial
from src.agente_prospector.controlo_react.reaccoes.recolher.evitar_memoria import EvitarMemoria 


class Recolher(Hierarquia):
    def _definir_reaccoes(self):
        #=======================================================================
        # return [AproximarAlvo(), EvitarObstaculo(),EvitarMemoria(0.9), SeguirPotencial(), Vaguear()]
        #=======================================================================
        return [AproximarAlvo(), EvitarObstaculo(),EvitarMemoria(0.9),SeguirPotencial(), Vaguear()]
    

        