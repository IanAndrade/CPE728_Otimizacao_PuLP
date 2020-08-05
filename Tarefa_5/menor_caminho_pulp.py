# Tarefa 5: Caminho mais curto - PuLP
# Autor: Ian Henriques de Andrade
# Exemplo numérico: Exemplo  mostrado na aula 10 - Problema do Caminho mais curto

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from pulp import*
s='1'
t='9'
#Lista de Nós
nodeList = ['1','2','3','4','5','6','7','8','9']
#Lista de Arestas 
verticesList = [('1','2'),('2','4'),('4','8'),('8','9'),('1','3'),('3','4'),('3','5'),('3','6'),('3','7'),
    ('5','9'),('5','7'),('6','1'),('7','6'),('9','7')]

custo = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
j=0
dic_custo={}
for i in verticesList:
    dic_custo[i] = custo[j]
    j=j+1
print('dicionario dos vertices e custos:', dic_custo)

DG=nx.DiGraph() # make a directed graph (digraph)

# DG.add_nodes_from(['1','2','3','4','5','6','7','8','9']) # add nodes
DG.add_nodes_from(nodeList) # add nodes

# DG.add_edges_from([('1','2'),('2','4'),('4','8'),('8','9'),('1','3'),('3','5'),('3','7'),
#     ('3','6'),('5','9'),('5','7'),('1','6'),('6','7'),('7','9')])
DG.add_edges_from(verticesList)

# nx.set_edge_attributes(DG,{('1','2'): 100,('2','4'): 10,('4','8'): 10,('8','9'): 100,('1','3'): 100,('3','5'): 25,('3','7'): 100,('3','6'): 10,('5','9'): 100,('5','7'): 10,('1','6'): 100,('6','7'): 25,('7','9'): 100}, 'capacity')
nx.set_edge_attributes(DG, dic_custo, 'custo')

print('menor caminho eh',nx.shortest_path(DG, s, t, weight='custo'))
nx.draw(DG,with_labels=True)
plt.show()

#Verifica quantos nós temos no grafo
print('len(nodeList)',len(nodeList))
#Cria uma matriz de ones de acordo com o numero de nós no exemplo = 9x9
custo_todos = np.ones((len(nodeList),len(nodeList)),dtype=int)
#Multiplica todos os valores dessa matriz por 100 (arbitrariamente) para ser um custo muito alto os nós que não tem ligação!
custo_todos=custo_todos*100
print('custo_todos',custo_todos)
#Cria o dicionario
dict_vertices_custo = makeDict((nodeList,nodeList),custo_todos,0)
print('dict_vertices_custo',dict_vertices_custo)
#Preenche os valores de capacidade!
for (u, v, c) in DG.edges.data('custo'):
    print('u',u)
    print('v',v)
    print('c',c)
    dict_vertices_custo[u][v]=c
# #Além disso, coloca custo 0 para os nós s e t
# dict_vertices_custo[s][s]=1
# dict_vertices_custo[t][t]=-1
print('dict_vertices_custo NOVO',dict_vertices_custo)

#Definição do Problema
prob = LpProblem("Menor_Caminho",LpMinimize)

variaveisX = LpVariable.dicts("X",(nodeList,nodeList),0,None,LpInteger)

#Criação de tuplas para representar todas as combinações possíveis
tuplasnodes = [(i,j) for i in nodeList for j in nodeList] #Ex: ("DC_1","PTT_1")
print('tuplasnodes = ', tuplasnodes)
#Definição da Função Objetivo!
prob += lpSum([dict_vertices_custo[i][j]*variaveisX[i][j] for (i,j) in tuplasnodes]),"Menor_Caminho"

#Restrições de conservação de fluxo!!
for i in nodeList:
    var_aux = ""
    for j in nodeList:
        var_aux += lpSum(variaveisX[i][j] - variaveisX[j][i])
    if (i == s):
        prob += var_aux == 1,"restricao_conservacao_fluxo_%s"%i
    elif (i == t):
        prob += var_aux == -1,"restricao_conservacao_fluxo_%s"%i
    else:
        prob += var_aux == 0,"restricao_conservacao_fluxo_%s"%i

prob.writeLP("Menor_caminho.lp")
prob.solve()
print("Status:",LpStatus[prob.status])

for v in prob.variables():
    if(v.varValue == 1):
        print(v.name,"=",v.varValue)

print("O Menor caminho pelo PuLP eh = ", value(prob.objective))
