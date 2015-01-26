'''
Created on 28/03/2014

@author: ASUS
'''

import sys
sys.path.append("..")

import psa
from agente_prospector.agente.agente_prospector import AgenteProspector
from src.agente_prospector.controlo_react.controlo_recolher import ControloRecolher

#Iniciacao da PSA no ambiente definido como parametro do metodo
psa.iniciar("amb/amb3.das")
#Instanciacao do Controlo a passar ao agente
#Este controlo define as reaccoes do agente mediante o ambiente percepcionado
controlo = ControloRecolher()        
#Instanciacao do agente
agente = AgenteProspector(controlo)
psa.executar(agente)