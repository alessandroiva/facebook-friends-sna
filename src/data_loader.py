import networkx as nx
import os

def load_graph(path='data/facebook_edges.txt'):
    """Loads the graph from the edge list file."""
    if not os.path.exists(path):
        # Fallback for relative paths if run from src or root
        if os.path.exists('../data/facebook_edges.txt'):
            path = '../data/facebook_edges.txt'
        else:
             print(f"Warning: Data file not found at {path}")

    list_edges = []
    with open(path, 'r') as dataset:
        for line in dataset:
            n1, n2 = line.split(" ")
            list_edges.append((int(n1), int(n2)))
    
    graph = nx.from_edgelist(list_edges)
    return graph, list_edges

def get_subgraph(graph, start_node=4023):
    """
    Extracts a subgraph starting from start_node (level 2 connections).
    As described in the analysis: node n + neighbors + neighbors of neighbors.
    """
    if start_node not in graph:
        return None
        
    s_edges = []
    level_i = [(start_node, k) for k in list(graph[start_node])]
    nodes_1 = [i[1] for i in level_i]
    
    level_ii = []
    for node in nodes_1:
         for neighbor in graph[node]:
             level_ii.append((node, neighbor))

    s_edges.extend(level_i)
    s_edges.extend(level_ii)
    s_graph = nx.from_edgelist(s_edges)
    return s_graph
