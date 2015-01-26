# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 17:51:58 2014

@author: namm
"""

class Reaccao:
    
    def _detectar_estimulo(self, percepcao):
        raise NotImplementedError
        # return estimulo
        
    def _gerar_resposta(self, estimulo):
        raise NotImplementedError
        # return accao
    
    def activar(self, percecao):
        estimulo = self._detectar_estimulo(percecao)
        if estimulo is not None:
            resposta = self._gerar_resposta(estimulo)
            return resposta
    

    
