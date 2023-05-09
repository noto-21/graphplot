from Node import Node

class Graph:
    def __init__(self):
        self.nodes = {}
    
    def add_node(self, identifier):
        node = Node(identifier)
        self.nodes[identifier] = node
    
    def add_edge(self, node1, node2):
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)
        self.nodes[node1].add_edge(node2)
        self.nodes[node2].add_edge(node1)