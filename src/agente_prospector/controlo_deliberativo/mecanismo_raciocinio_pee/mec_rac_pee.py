'''
Created on 23/05/2014

@author: ASUS
'''
import psa
from src.agente_prospector.controlo_deliberativo.mecanismo_raciocinio import MecanismoRaciocinio
from src.agente_prospector.controlo_deliberativo.mecanismo_raciocinio_pee.problema_rac_pee import ProblemaRacPee
from psa.actuador import MOVER
from psa.util import mover
import time


from src.pee.procura_largura import ProcuraLargura
from src.pee.procura_custo_uniforme import ProcuraCustoUniforme
from src.pee.procura_profundidade_limitada import ProcuraProfundidadeLimitada
from src.pee.procura_iterativa import ProcuraIterativa
from src.pee.procura_sofrega import ProcuraSofrega
from src.pee.procura_AA import Procura_AA

class MecRacPee (MecanismoRaciocinio):
    
    def __init__(self):
        self._custo=0
        self._tempo_in = time.time()
        self._tempo_procura = None
        self._plano = None
        #self._procura = ProcuraLargura()
        #self._procura = ProcuraCustoUniforme()
        self._procura = ProcuraProfundidadeLimitada()
        #self._procura = ProcuraIterativa()
        #self._procura = ProcuraSofrega()
       # self._procura = Procura_AA()
        

    def planear(self, crencas, capacidades, intencoes):
        #Problema precisa de posAgente - que esta no mover
        #                    objectivo - intencoes
        #                    operadores - capacidades (Mover)
        pos_agente = crencas.pos_agente()
        problema = ProblemaRacPee(pos_agente, capacidades, intencoes[0])
        solucao = self._procura.procurar( problema, 15000) ##lista nos (estado, operador-Mover)
        self._plano=list()
        for no in solucao:
            if no._operador is not None:
                self._plano.append(no._operador)
        psa.vismod.elementos(crencas._elementos)
        psa.vismod.plano(pos_agente,self._plano)
                 
    
    def executar(self, crencas = None):
        if self._plano: #assim abrange o caso de n ser none nem lista vazia
            operador = self._plano.pop(0)
            pos_apos_estado = mover(crencas.pos_agente(), operador.getAngulo())
            self._custo += operador.custo( crencas.pos_agente(), pos_apos_estado)
            self._tempo_procura = time.time()
            self._mostrar_informacao()
            return MOVER(operador.getAngulo())
        
    def _mostrar_informacao(self):
        max_len_fronteira, max_len_explorados = self._procura.get_numero_nos();
        psa.info("Custo = "+str(round(self._custo,2))+"  Tempo = "+str(round(self._tempo_procura-self._tempo_in,2))+" s"+"  Max front de exp  = "+str(max_len_fronteira)+"  Max de estados explorados = "+str(max_len_explorados))
            