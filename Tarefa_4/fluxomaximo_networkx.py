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