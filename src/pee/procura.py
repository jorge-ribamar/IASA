'''
Created on 11/04/2014

@author: ASUS
'''

from src.pee.memoria_exploracao import MemoriaExploracao
from src.pee.no import No

class Procura(object):
    def __init__(self):
        self._memoria_exp = MemoriaExploracao()
        self._problema = None
        self._max_len_fronteira = 0
        self._max_len_explorados = 0
    
    def procurar(self, Problema):
        self._problema = Problema
        self._memoria_exp.iniciar()
        self._memoria_exp.inserir(No(Problema.estado_inicial(),None,None), 0)          
        while not self._memoria_exp.fronteira_vazia():
            no = self._memoria_exp.remover()
            if not Problema.objectivo(no._estado):
                self.expandir(no)
            else:
                return no.gerar_percurso()
        #return Percurso
    
    def expandir(self, no):
        #por cada no e posto na memoria exploracao
        for operador in self._problema.operadores():
            novo_estado = operador.aplicar(no._estado)
            if novo_estado is not None:
                novo_no = No(novo_estado, operador, no)
                self.expandir_fronteira(novo_no)
                max_len_fronteira, max_len_explorados = self._memoria_exp.get_numero_nos()
                if (self._max_len_fronteira<max_len_fronteira):
                    self._max_len_fronteira = max_len_fronteira
                if (self._max_len_explorados < max_len_explorados):
                    self._max_len_explorados = max_len_explorados
                
                
    def expandir_fronteira(self, no):
        self._memoria_exp.inserir(no, self.ordem(no))
    
    def ordem(self, no):
        #este e abstract
        raise NotImplementedError
        #return float
        
    def get_numero_nos(self):
        return self._max_len_fronteira, self._max_len_explorados