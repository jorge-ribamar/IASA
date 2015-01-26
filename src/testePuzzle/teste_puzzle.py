'''
Created on 08/05/2014

@author: ASUS
'''

from src.pee.procura_profundidade import ProcuraProfundidade
from src.pee.procura_largura import ProcuraLargura
from src.testePuzzle.problema_puzzle import ProblemaPuzzle
from src.pee.procura_custo_uniforme import ProcuraCustoUniforme
from src.pee.procura_sofrega import ProcuraSofrega
from src.pee.procura_AA import Procura_AA
from src.pee.procura_profundidade_limitada import ProcuraProfundidadeLimitada
from src.pee.procura_iterativa import ProcuraIterativa

import time



#puz_ini = ((1,2,3),(8,4,5),(6,7,0))

puz_ini = ((8,4,5),(6,1,2),(3,7,0))


puz_obj = ((1,2,3),(4,5,6),(7,8,0))

problema= ProblemaPuzzle(puz_ini,puz_obj)
#procura = ProcuraProfundidade()
#procura = ProcuraLargura()
#procura = ProcuraCustoUniforme()
procura = ProcuraProfundidadeLimitada()
#procura = ProcuraIterativa()
#procura = ProcuraSofrega()
#procura = Procura_AA()

#precurso = procura.procurar(problema)
##ProcuraProfundidadeLimitada
t0 = time.time()
precurso = procura.procurar(problema, 15000) #29596
t1=time.time()
##Procura ProcuraIterativa
#t0 = time.time()
#precurso = procura.procurar(problema, 15000, 15000/3)
#t1=time.time()
##Outras Procuras
# t0 = time.time()
# precurso = procura.procurar(problema)
# t1=time.time()


if precurso is not None:
    for step in precurso:
        print step._estado
    print "Custo=" + str(precurso[-1].custo)
    max_len_fronteira, max_len_explorados = procura.get_numero_nos()
    print "Fronteira = "+str(max_len_fronteira)+" Memoria = "+str(max_len_explorados)
    print "Tempo = "+str(round(t1-t0,2))
else:
    print "Percurso is None";


