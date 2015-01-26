# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 17:52:01 2014

@author: namm
"""

class Controlo:
    #interface nao tem construtor
    #Obrigação d eimplementação do método nas classes derivadas
    #recebe uma percepção e devolve uma accão, mediante o processamento interno
    def processar(self, percepcao):
        raise NotImplementedError #
        
