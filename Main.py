from Graph import Graph

import networkx as nx
import matplotlib.pyplot as plt

graph = Graph()

graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)
graph.add_node(6)
graph.add_node(7)

graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 1)
graph.add_edge(2, 4)
graph.add_edge(1, 5)
graph.add_edge(5, 1)
graph.add_edge(6, 7)
graph.add_edge(6, 4)
graph.add_edge(5, 7)

nx_graph = nx.Graph()
for identifier in graph.nodes:
    nx_graph.add_node(identifier)
for identifier in graph.nodes:
    for adjacent_node in graph.nodes[identifier].adjacent_nodes:
        nx_graph.add_edge(identifier, adjacent_node)

pos = nx.spring_layout(nx_graph)
nx.draw(nx_graph, pos, with_labels=True, font_weight='bold')
nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels={(1, 2): "1-2", (2, 3): "2-3", (3, 1): "3-1", (2, 4): "2-4", (1, 5): "1-5", (5, 7): "5-7", (6, 7): "6-7", (6, 4): "6-4", (5, 1): "5-1"})
plt.show()