'''
Created on 15/05/2014

@author: ASUS
'''
from src.pee.problema import Problema


class ProblemaHeuristico(Problema):
    
    def heuristica(self, estado):
        raise NotImplementedError
        #abstract
