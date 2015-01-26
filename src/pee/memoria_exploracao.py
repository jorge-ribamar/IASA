'''
Created on 11/04/2014

@author: ASUS
'''
import heapq

class MemoriaExploracao:
    def __init__(self):
        self.iniciar()
    
    def iniciar(self):
        self._fronteira=[]
        self._explorados = {}
    
    def inserir(self, No, Ordem):
        heapq.heappush(self._fronteira, (Ordem, No))
        self._explorados[No._estado] = No
    
    def remover(self):
        return heapq.heappop(self._fronteira)[1]
        #return No
    
    def fronteira_vazia(self):
        return len(self._fronteira)==0
        #return Boolean
        
    def obter(self, no):
        return self._explorados.get(no._estado)
        #return no_menor
        
    def get_numero_nos(self):
        return len(self._fronteira), len(self._explorados)