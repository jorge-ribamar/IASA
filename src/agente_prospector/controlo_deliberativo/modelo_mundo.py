'''
Created on 23/05/2014

@author: ASUS
'''

class ModeloMundo():
    
    def __init__(self):
        self._pos_agente = None
        self._elementos = {}

    def actualizar(self, percepcao):
        self._pos_agente = percepcao.posicao
        self._elementos  = percepcao.imagem
    
    def elementos_tipo(self, tipo):
        elementos_tipo = list()
        for (pos, tipo_pos) in self._elementos.items():
            if tipo_pos == tipo:
                elementos_tipo.append((pos, tipo_pos))
        return elementos_tipo
        #return List<Elemtnto> (tuplo pos, tipo)
        
    def pos_agente(self):
        return self._pos_agente
        #return posicao
        
    def pos_valida(self, pos):
        elemento = self._elementos.get(pos)
        return  elemento is not None and elemento!="obst"
        
    def posicoes(self):
        return self._elementos.keys()
    
    
        #=======================================================================
        # obst
        # agente
        # vazio
        # alvo
        #=======================================================================
        
        