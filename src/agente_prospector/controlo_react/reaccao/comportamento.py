'''
Created on 27/03/2014

@author: Portatil
'''
import sys
sys.path.append("..")
from agente_prospector.controlo_react.reaccao.reaccao import Reaccao

class Comportamento(Reaccao):
    
    
    def __init__(self):
        self._reaccoes = self._definir_reaccoes()  
        
    
    def _definir_reaccoes(self):
        # return self.reaccoes  #[]
        raise NotImplementedError

    def _seleccionar_accao(self,respostas):  #array de accoes
        raise NotImplementedError
        
    
        
    def activar(self, percepcao):
        respostas=[]
        for reacao in self._reaccoes:
            accao = reacao.activar(percepcao)
            if accao is not None:
                respostas.append(accao) 
        if respostas:
            accao_selecionada = self._seleccionar_accao(respostas)
            return accao_selecionada
    