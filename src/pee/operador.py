'''
Created on 11/04/2014

@author: ASUS
'''
class Operador:
    #e uma interface
    
    def aplicar(self, Estado):
        raise NotImplementedError
        #return Estado
    
    def custo(self, Estado, Estado_sucessor):
        raise NotImplementedError
        #return float