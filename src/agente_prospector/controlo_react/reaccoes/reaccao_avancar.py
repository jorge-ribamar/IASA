# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 17:52:01 2014

@author: namm
"""

import sys
sys.path.append("..")
from agente_prospector.controlo_react.reaccao.reaccao import Reaccao

class ReaccaoAvancar(Reaccao):
    
    def _detectar_estimulo(self, percepcao):
        return True # percepção vai estar sempre activa
        
    def _gerar_resposta(self, estimulo):
        return (1,0) #avançar, um passo na direcção zero (horizontal)
    
