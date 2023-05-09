class Node:
    def __init__(self, identifier):
        self.identifier = identifier
        self.adjacent_nodes = []
    
    def add_edge(self, node):
        self.adjacent_nodes.append(node)