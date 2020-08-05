# Tarefa 5: Caminho mais curto - NetworkX
# Autor: Ian Henriques de Andrade
# Exemplo numérico: Exemplo  mostrado na aula 10 - Problema do Caminho mais curto
import networkx as nx
import matplotlib.pyplot as plt
# from pulp import*
s='2'
t='6'
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