'''
Created on 11/04/2014

@author: ASUS
'''

class No:
    def __init__(self, Estado, Operador, Antecessor=None):
        self._no_antecessor = Antecessor
        self._estado = Estado
        self._operador = Operador
        if self._no_antecessor is not None:
            self._profundidade = self._no_antecessor._profundidade+1
            self.custo = self._no_antecessor.custo + Operador.custo(Antecessor._estado, self._estado)
        else:
            self._profundidade = 0
            self.custo=0
    
    def gerar_percurso(self):
        percurso = []
        no_actual=self
        while no_actual is not None:
            percurso.insert(0,no_actual)
            no_actual = no_actual._no_antecessor
        return percurso
        #return Percurso