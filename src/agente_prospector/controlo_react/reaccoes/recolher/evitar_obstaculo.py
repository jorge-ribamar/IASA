from agente_prospector.controlo_react.reaccao.reaccao import Reaccao
import psa
from psa.actuador import ESQ, DIR, FRT


class EvitarObstaculo(Reaccao):

    def _detectar_estimulo(self, percepcao):
        if percepcao[FRT].contacto and  percepcao[FRT].obstaculo:
            return True
        
    def _gerar_resposta(self, estimulo):
        return (0,ESQ)