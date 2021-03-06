# Tarefa 4: Fluxo Máximo - PuLP
# Autor: Ian Henriques de Andrade
# Exemplo numérico: Exemplo de redes de computadores mostrado na aula 09 - Problema do Fluxo Máximo
# Resposta do exemplo numérico: 135

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from pulp import*
# Tarefa 4: Fluxo Máximo - NetworkX
# Autor: Ian Henriques de Andrade
# Exemplo numérico: Exemplo de redes de computadores mostrado na aula 09 - Problema do Fluxo Máximo
# Resposta do exemplo numérico: 135 (p/ s = 1 e t = 9)
import networkx as nx
import matplotlib.pyplot as plt
# from pulp import*
s='1'
t='9'
#Lista de Nós
nodeList = ['1','2','3','4','5','6','7','8','9']
#Lista de Arestas 
verticesList = [('1','2'),('2','4'),('4','8'),('8','9'),('1','3'),('3','5'),('3','7'),
    ('3','6'),('5','9'),('5','7'),('1','6'),('6','7'),('7','9')]

#('1','2'): 100,
#('2','4'): 10,
#('4','8'): 10,
#('8','9'): 100,
#('1','3'): 100,
#('3','5'): 25,
#('3','7'): 100,
#('3','6'): 10,
#('5','9'): 100,
#('5','7'): 10,
#('1','6'): 100,
#('6','7'): 25,
#('7','9'): 100,
Fluxo_max_verticesList = [100,10,10,100,100,25,100,10,100,10,100,25,100]

j=0
dic_capacidade={}
for i in verticesList:
    dic_capacidade[i] = Fluxo_max_verticesList[j]
    j=j+1
print('dicionario dos vertices e capacidades:', dic_capacidade)

DG=nx.DiGraph() # make a directed graph (digraph)

# DG.add_nodes_from(['1','2','3','4','5','6','7','8','9']) # add nodes
DG.add_nodes_from(nodeList) # add nodes

# DG.add_edges_from([('1','2'),('2','4'),('4','8'),('8','9'),('1','3'),('3','5'),('3','7'),
#     ('3','6'),('5','9'),('5','7'),('1','6'),('6','7'),('7','9')])
DG.add_edges_from(verticesList)

# nx.set_edge_attributes(DG,{('1','2'): 100,('2','4'): 10,('4','8'): 10,('8','9'): 100,('1','3'): 100,('3','5'): 25,('3','7'): 100,('3','6'): 10,('5','9'): 100,('5','7'): 10,('1','6'): 100,('6','7'): 25,('7','9'): 100}, 'capacity')
nx.set_edge_attributes(DG, dic_capacidade, 'capacity')

print('fluxo maximo eh',nx.maximum_flow_value(DG,s,t))

nx.draw(DG,with_labels=True)
plt.show()

#Verifica quantos nós temos no grafo
print('len(nodeList)',len(nodeList))
#Cria uma matriz de zeros de acordo com o numero de nós no exemplo = 9x9
Fluxo_max_todos = np.zeros((len(nodeList),len(nodeList)),dtype=int)
print('Fluxo_max_todos',Fluxo_max_todos)
#Cria o dicionario
dict_vertices_flux_max = makeDict((nodeList,nodeList),Fluxo_max_todos,0)
print('dict_vertices_flux_max',dict_vertices_flux_max)
#Preenche os valores de capacidade!
for (u, v, c) in DG.edges.data('capacity'):
    print('u',u)
    print('v',v)
    print('c',c)
    dict_vertices_flux_max[u][v]=c
print('dict_vertices_flux_max NOVO',dict_vertices_flux_max)

#Definição do Problema
prob = LpProblem("Fluxo_Maximo",LpMaximize)

variaveisX = LpVariable.dicts("X",(nodeList,nodeList),0,None,LpInteger)

#Criação de tuplas para representar todas as combinações possíveis
tuplasnodes = [(a,b) for a in nodeList for b in nodeList] #Ex: ("DC_1","PTT_1")
print('tuplasnodes = ', tuplasnodes)
#Definição da Função Objetivo!
prob += lpSum(variaveisX[s][i] for i in nodeList),"Fluxo_maximo"

#Restrições do limite inferior (0)
for (a,b) in tuplasnodes:
    prob += variaveisX[a][b] >= 0,"restricao_lim_infs_%s_%s"%(a,b)

#Restrições do limite superior!
for (a,b) in tuplasnodes:
    prob += variaveisX[a][b] <= dict_vertices_flux_max[a][b],"restricao_lim_sup_%s_%s"%(a,b)

#Restrições de conservação de fluxo!!
for b in nodeList:
    if (b != s) and (b != t):
        prob += lpSum([variaveisX[b][a] - variaveisX[a][b] for a in nodeList])==0,"restricao_conservacao_fluxo_%s_%s"%(a,b)

prob.writeLP("Fluxo_maximo.lp")
prob.solve()
print("Status:",LpStatus[prob.status])

for v in prob.variables():
    print(v.name,"=",v.varValue)

print("O Fluxo Maximo Pelo PuLP eh = ", value(prob.objective))
