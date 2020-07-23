# Tarefa 3: Aquecimento no NetworkX - Grafo não Direcionado
# Autor: Ian Henriques de Andrade
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
# G.add_edge(1, 3, weight=7, capacity=15, length=342.7)
G.add_edge('1', '2', weight = 2)
G.add_edge('1', '4', weight = 2)
G.add_edge('2', '3', weight = 2)
G.add_edge('2', '5', weight = 2)
G.add_edge('4', '5', weight = 2)
G.add_edge('3', '6', weight = 2)
G.add_edge('5', '6', weight = 2)
# G.add_edge('B', 'D', weight=2)
# G.add_edge('A', 'C', weight=3)
# G.add_edge('C', 'D', weight=4)
print(nx.shortest_path(G, '1', '6', weight='weight'))
nx.draw(G,with_labels=True)
plt.show()