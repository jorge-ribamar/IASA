'''
Created on 11/04/2014

@author: ASUS
'''

class Problema:
    #e uma interface
    
    def estado_inicial(self):
        raise NotImplementedError
        #return Estado
       
    def objectivo(self,Estado):
        raise NotImplementedError
        #return Boolean
    
    def operadores(self):
        raise NotImplementedError
        #return Operadors []