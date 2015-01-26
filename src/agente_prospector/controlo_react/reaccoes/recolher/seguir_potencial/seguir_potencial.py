'''
Created on 03/04/2014

@author: ASUS
'''
import sys
sys.path.append("..")
from agente_prospector.controlo_react.reaccao.seleccao import Seleccao
from src.agente_prospector.controlo_react.reaccoes.recolher.seguir_potencial.seguir_portencial_dir import SeguirPotencialDir
from psa.actuador import ESQ, DIR, FRT


class SeguirPotencial(Seleccao):
    
    def _definir_reaccoes(self):
        return [SeguirPotencialDir(0,ESQ), SeguirPotencialDir(0,DIR), SeguirPotencialDir(1,FRT)]
    
