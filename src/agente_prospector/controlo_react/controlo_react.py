# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 17:52:01 2014

@author: namm
"""
import sys
sys.path.append("..")
from agente_prospector.agente.controlo import Controlo

from agente_prospector.controlo_react.reaccoes.reaccao_avancar import ReaccaoAvancar


class ControloReact(Controlo):
    
    def __init__(self):
        self._reaccao = ReaccaoAvancar()
    
    def processar(self, percepcao):
        accao = self._reaccao.activar(percepcao)
        return accao
        
