# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 18:15:31 2014

@author: namm
"""
import sys
sys.path.append("..")
from psa.agente import Agente

class AgenteProspector(Agente):

    def __init__(self, controlo):
        self._controlo=controlo


    def executar(self):
        percepcao = self.sensor_multiplo.detectar()
        accao = self._controlo.processar(percepcao)
        if accao is not None:
            self.actuador.actuar(accao)



