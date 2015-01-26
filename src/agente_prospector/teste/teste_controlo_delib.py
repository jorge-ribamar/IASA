'''
Created on 30/05/2014

@author: ASUS
'''
import sys
sys.path.append("..")

import psa
from agente_prospector.agente.agente_prospector import AgenteProspector
from src.agente_prospector.controlo_deliberativo.controlo_deliberativo import ControloDeliberativo
from src.agente_prospector.controlo_deliberativo.mecanismo_raciocinio_pee.mec_rac_pee import MecRacPee
from src.agente_prospector.controlo_deliberativo.mecanismo_raciocinio_pdm.mec_rac_pdm import MecRacPDM

psa.iniciar("amb/amb1.das")
mec_rac = MecRacPDM()
#mec_rac = MecRacPee()
controlo = ControloDeliberativo(mec_rac)        
agente = AgenteProspector(controlo)
psa.executar(agente)
