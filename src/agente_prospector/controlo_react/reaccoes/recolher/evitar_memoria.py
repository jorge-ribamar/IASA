'''
Created on 04/04/2014

@author: ASUS
'''

import sys
sys.path.append("..")
import psa
from psa.actuador import FRT
from agente_prospector.controlo_react.reaccao.reaccao import Reaccao

class EvitarMemoria(Reaccao):
    def __init__(self, factorRetencao):
        self._factorRetencao = factorRetencao
        self._memoria = {}
        self._limiarEsquecimento = 0.1
    
    def _gerar_resposta(self, posicao):
        memoria = self._activar_memoria(posicao)
        if memoria is not None:
            return (1,FRT)
            
    def _activar_memoria(self, posicao):
        memoriaPosicao = self._recordar(posicao)
        self._memorizar(posicao)
        self._esquecer()
        return memoriaPosicao

    def _recordar(self, posicao):
        return self._memoria.get(posicao)
        
    def _detectar_estimulo(self, percepcao):
        return percepcao.posicao
    
    def _memorizar(self, posicao):
        self._memoria[posicao] = 1
    
    def _esquecer(self):
        psa.vismod.limpar()
        for posicao in self._memoria.keys():
            self._memoria[posicao] *= self._factorRetencao
            self._mostrar_memoria(posicao)
            if self._memoria[posicao] <= self._limiarEsquecimento:
                del self._memoria[posicao]
            

    def _mostrar_memoria(self, posicao):
        corMem=(0,0,255*self._memoria[posicao])
        psa.vismod.rect(posicao,cor=corMem, linha = 0)
        
                