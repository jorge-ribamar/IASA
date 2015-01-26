'''
Created on 22/05/2014

@author: ASUS
'''

from src.agente_prospector.agente.controlo import Controlo
from src.agente_prospector.controlo_deliberativo.mecanismo_raciocinio_pee.problema_rac_pee import ProblemaRacPee
from src.agente_prospector.controlo_deliberativo.mover import Mover
from src.agente_prospector.controlo_deliberativo.modelo_mundo import ModeloMundo
import psa
from psa.util import dist

class ControloDeliberativo(Controlo):
    
    def __init__(self, mecanismo_raciocinio):
        self._crencas = ModeloMundo()
        self._desejos = None #vai ser lista de posicoes
        self._intencoes = None #vai ser lista de posicoes 
        self._capacidades = [Mover(self._crencas, angulo) for angulo in psa.dirmov()]
        self._mecanismo_raciocinio = mecanismo_raciocinio
    
    def processar(self, per):
        self._actualizar_crencas(per)
        if self._reconsiderar():
            self._deliberar() #aqui tneho intencoes
            if len(self._intencoes)>0:
                self._mecanismo_raciocinio.planear(self._crencas, self._capacidades, self._intencoes)
        return self._mecanismo_raciocinio.executar(self._crencas) #e uma accao
    
    def _actualizar_crencas(self, percepcao):
        #metodo de fachada
        self._crencas.actualizar(percepcao)
    
    def _deliberar(self):
        self._gerar_opcoes()
        if self._desejos is not None:
            self._selecionar_opcoes()
        else:
            self._intencoes = None
                
    def _gerar_opcoes(self):
        elementos_alvo = self._crencas.elementos_tipo("alvo")
        self._desejos = map( lambda (pos,elem): pos, elementos_alvo)

    
    def _selecionar_opcoes(self):
        pos_agente = self._crencas.pos_agente()
        f_avaliacao = lambda pos_desejo : dist(pos_desejo, pos_agente)
        self._intencoes = sorted(self._desejos, key = f_avaliacao)
    
    def _reconsiderar(self):
        return True #caso extremo do agente cauteloso
        #return boolean
        
        