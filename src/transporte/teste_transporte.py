'''
Created on 24/04/2014

@author: ASUS
'''
from src.pee.procura_profundidade import ProcuraProfundidade
from src.pee.procura_largura import ProcuraLargura
from src.transporte.problema_transporte import ProblemaTransporte

#===============================================================================
# #sem ciclos
# tabela_ligacoes=[(0,1,5),
#                  (0,2,25),
#                  (1,3,12),
#                  (1,6,5),
#                  (2,4,30),
#                  (3,2,10),
#                  (3,5,5),
#                  (4,3,2),
#                  (5,6,8),
#                  (5,4,10),
#                  (6,3,15)]
#===============================================================================

#com ciclos
tabela_ligacoes=[(0,1,5),
                  (0,2,25),
                  (1,3,12),
                  (1,6,5),
                  (2,4,30),
                  (3,5,5),
                  (3,2,10),
                  (4,3,2),
                  (5,6,8),
                  (5,4,10),
                  (6,3,15)]

estado_inicial=0
objectivo=4

problema= ProblemaTransporte(estado_inicial,objectivo,tabela_ligacoes)
procura = ProcuraProfundidade()
#procura = ProcuraLargura()
precurso = procura.procurar(problema)

for a in precurso:
    print a._estado
print "Custo=" + str(precurso[-1]._custo)