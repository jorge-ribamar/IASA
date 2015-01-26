'''
Created on 05/06/2014

@author: ASUS
'''
# e uma interface
class ModeloPDM:
    
    def S(self):
        raise NotImplementedError

    # s e estado, a operador e sn prox estado
    
    def A(self, s):
        raise NotImplementedError
    
    def T(self, s, a, sn):
        raise NotImplementedError
    
    def R(self, s, a, sn):
        raise NotImplementedError

    def gama(self):
        raise NotImplementedError
    
    def suc(self, s,a): #significa sucessor
        #produz s', o novo estado
        raise NotImplementedError
        