'''
Created on 23/05/2014

@author: ASUS
'''
import psa
from src.agente_prospector.controlo_deliberativo.mecanismo_raciocinio_pdm.modelo_rec_alvos import ModeloRecAlvos
from src.agente_prospector.controlo_deliberativo.mecanismo_raciocinio import MecanismoRaciocinio
from src.agente_prospector.controlo_deliberativo.mecanismo_raciocinio_pdm.modelo_rec_alvos import ModeloRecAlvos
from src.PDM.pdm import PDM
from psa.actuador import MOVER


class MecRacPDM (MecanismoRaciocinio):
    
    def __init__(self):
        self._pdm = PDM()
        self._epsilon = 1
        self._politica = None 

    def planear(self, crencas, capacidades, intencoes):
        self._politica = None 
        modelo = ModeloRecAlvos(crencas,capacidades ,intencoes )
        if intencoes is not None:
            un = self._pdm.utilidade(modelo, self._epsilon)
            self._politica = self._pdm.politica(modelo, un)
            psa.vismod.campo(un)
            psa.vismod.politica(self._politica) # politica e um dicionario cujas chaves sao o estado, e o valor e a cacao  
    
    def executar(self, crencas = None):
        if self._politica is not None:
            acao =  self._politica[crencas.pos_agente()]
            return MOVER(acao.getAngulo())
