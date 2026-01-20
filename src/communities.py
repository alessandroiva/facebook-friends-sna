import networkx as nx
from networkx.community import girvan_newman, greedy_modularity_communities, asyn_lpa_communities, quality

def analyze_communities(graph):
    """
    Runs Bridge Removal (Girvan-Newman), Modularity Optimization, and Label Propagation.
    Returns the partitions.
    """
    print("Running Girvan-Newman (Bridge Removal)...")
    comp = girvan_newman(graph)
    
    max_modularity = -1
    best_partition = None
    
    try:
        closest_partition = tuple(sorted(c) for c in next(comp)) 
        best_partition = closest_partition
        max_modularity = quality.modularity(graph, best_partition)
    except StopIteration:
        best_partition = []
        
    print("Running Greedy Modularity Optimization...")
    modularity_opt = list(greedy_modularity_communities(graph))
    
    print("Running Label Propagation...")
    label_p = list(asyn_lpa_communities(graph, seed=42))
    
    results = {
        "BridgeRemoval": best_partition,
        "ModularityOpt": modularity_opt,
        "LabelProp": label_p
    }
    return results

def get_modularity_score(graph, partition):
    return quality.modularity(graph, partition)
