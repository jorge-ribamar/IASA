# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 17:52:01 2014

@author: namm
"""
import sys
sys.path.append("..")

import psa
from agente_prospector.agente.agente_prospector import AgenteProspector
from agente_prospector.controlo_react.controlo_react import ControloReact

psa.iniciar("amb/amb1.das")
controlo = ControloReact()        
agente = AgenteProspector(controlo)
psa.executar(agente)
