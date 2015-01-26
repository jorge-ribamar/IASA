'''
Created on 27/03/2014

@author: Portatil
'''
import sys
sys.path.append("..")
from agente_prospector.controlo_react.reaccao.comportamento import Comportamento

class Seleccao(Comportamento):
    
        def _seleccionar_accao(self,respostas):  #array de accoes
            respostas_prior = sorted(respostas)
            accao_selecionada = respostas_prior[-1]
            return accao_selecionada[1]