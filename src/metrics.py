import networkx as nx
import matplotlib.pyplot as plt

def compute_basic_metrics(graph):
    """Computes basic metrics: nodes, edges, average degree, density."""
    n_nodes = graph.number_of_nodes()
    n_edges = graph.number_of_edges()
    n_neighborhoods = 2 * n_edges
    
    if n_nodes > 1:
        avg_degree = n_neighborhoods / n_nodes
        density = avg_degree / (n_nodes - 1)
    else:
        avg_degree = 0
        density = 0
        
    return {
        "n_nodes": n_nodes,
        "n_edges": n_edges,
        "avg_degree": avg_degree,
        "density": density
    }

def transitivity_of(graph):
    """Custom transitivity implementation."""
    n_triangles = sum(list(nx.triangles(graph).values()))
    series_ki = 0
    for i in graph:
        degree_ki = len(graph[i])
        series_ki = series_ki + (degree_ki * (degree_ki - 1)) / 2
    
    if series_ki == 0:
        return 0
    return (n_triangles) / ((1/3) * series_ki)

def normalized_betweenness_of(g):
    """Custom Normalized Betweenness Centrality."""
    nodes = list(g.nodes())
    n_nodes = len(g)
    visited = []
    s_paths = {}
    
    # Step 1: Find valid paths > 2
    for i in nodes:
        for j in nodes:
            if i != j and ((i, j) not in visited and (j, i) not in visited):
                visited.append((i, j))
                try:
                    for p in nx.all_shortest_paths(g, source=i, target=j):
                        if len(p) > 2:
                            if (i, j) not in s_paths:
                                s_paths[(i, j)] = [p]
                            else:
                                s_paths[(i, j)].extend([p])
                except nx.NetworkXNoPath:
                    continue

    # Step 2: Calculate betweenness
    normalized_betweness = {}
    if n_nodes <= 2:
         denom = 1
    else:
         denom = ((n_nodes - 1) * (n_nodes - 2) / 2)
    
    ratio = 1 / denom

    for n in nodes:
        sommatory = 0
        for sp in s_paths:
            paths = s_paths[sp]
            n_inside_sp = 0
            n_of_sp = len(paths)
            for k in paths:
                # exclude source and target
                internal_nodes = k[1:-1]
                if n in internal_nodes:
                    n_inside_sp += 1
            sommatory += (n_inside_sp / n_of_sp)
        betweeness = 0.5 * sommatory
        normalized_betweness[n] = ratio * betweeness
        
    return normalized_betweness

def computation_cdf(centrality, title="CDF"):
    """Plots the Cumulative Distribution Function."""
    centralities = list(centrality.values())
    number_of = {}
    for i in centralities:
        if i not in number_of:
            number_of[i] = 1
        else:
            number_of[i] += 1
    number_of = dict(sorted(number_of.items()))
    
    tot_number = sum(list(number_of.values()))
    f = {}
    for i in number_of:
        f[i] = number_of[i] / tot_number
        
    f_values = list(f.values())
    cd_y = []
    cd_x = [i for i in f]
    for k in range(len(f_values)):
        cd_y.append(sum(f_values[k:]))
    
    plt.figure()
    plt.plot(cd_x, cd_y, '.')
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Cumulative Probability")
    # plt.show() # Return plot object or figure instead of showing immediately in non-interactive
    return plt
