import networkx as nx
import pandas as pd
import numpy as np

def compute_similarities(graph, listofnodes):
    """
    Computes Link Prediction indices: CN, JI, PA, AA, RA.
    """
    graphedges = set(graph.edges())
    cn = {}
    visited_n = set()
    
    node_list_int = [int(n) for n in listofnodes]
    
    neighbors = {n: set(graph.neighbors(n)) for n in node_list_int}
    degrees = {n: len(neighbors[n]) for n in node_list_int}

    pairs = []
    nodes = node_list_int
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u, v = nodes[i], nodes[j]
            if not graph.has_edge(u, v):
                pairs.append((u, v))

    data_rows = []
    indices = []

    for n1, n2 in pairs:
        common_neighbors = list(neighbors[n1].intersection(neighbors[n2]))
        
        num_cn = len(common_neighbors)
        
        union_len = len(neighbors[n1].union(neighbors[n2]))
        ji = num_cn / union_len if union_len > 0 else 0
        
        pa = degrees[n1] * degrees[n2]
        
        aa = 0
        ra = 0
        for z in common_neighbors:
            deg_z = degrees[z]
            if deg_z > 1:
                aa += 1 / np.log10(deg_z)
            if deg_z > 0:
                ra += 1 / deg_z
        
        data_rows.append([num_cn, ji, pa, aa, ra])
        indices.append((n1, n2))

    df = pd.DataFrame(data_rows, columns=['CN', 'JI', 'PA', 'AA', 'RA'], index=indices)
    return df

def min_max_scale(data):
    if np.max(data) == np.min(data):
        return data - data 
    return (data - np.min(data)) / (np.max(data) - np.min(data))
