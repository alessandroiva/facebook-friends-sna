import networkx as nx
import numpy as np
import random
from src.data_loader import load_graph, get_subgraph
from src.metrics import compute_basic_metrics, transitivity_of, normalized_betweenness_of
from src.pagerank import custom_pagerank
from src.communities import analyze_communities, get_modularity_score
from src.link_prediction import compute_similarities, min_max_scale
from src.diffusion import run_icm

def main():
    print("--- Facebook SNA Pipeline ---")
    
    # 1. Data Loading
    print("\n[1] Loading Graph...")
    graph, edges = load_graph()
    print(f"Full Graph: {graph.number_of_nodes()} nodes, {graph.number_of_edges()} edges")
    
    # 2. Subgraph Extraction
    print("\n[2] Extracting Subgraph (Ego Network of node 4023)...")
    s_graph = get_subgraph(graph, start_node=4023)
    if not s_graph:
        print("Error: Could not extract subgraph.")
        return
    print(f"Subgraph: {s_graph.number_of_nodes()} nodes, {s_graph.number_of_edges()} edges")
    
    # 3. Basic Metrics
    print("\n[3] Basic Metrics...")
    metrics = compute_basic_metrics(s_graph)
    print(metrics)
    
    trans_val = transitivity_of(s_graph)
    print(f"Transitivity: {trans_val}")
    
    # 4. Centrality (Betweenness)
    print("\n[4] Computing Betweenness Centrality (this may take a moment)...")
    bet_cen = normalized_betweenness_of(s_graph)
    print(f"Max Betweenness: {max(bet_cen.values())}")
    
    # 5. PageRank
    print("\n[5] Computing PageRank...")
    pagerank_vals, iters = custom_pagerank(s_graph, alpha=0.15) 
    print(f"Max PageRank: {max(pagerank_vals.values())} in {iters} iterations")
    
    # 6. Community Detection
    print("\n[6] Community Detection...")
    communities = analyze_communities(s_graph)
    for method, partition in communities.items():
        if partition:
            mod_score = get_modularity_score(s_graph, partition)
            print(f"{method}: {len(partition)} communities, Modularity: {mod_score:.4f}")
            
    # 7. Link Prediction
    print("\n[7] Link Prediction (Sample)...")
    print("Skipping full link prediction calculation for main execution speed (uncomment in script to run).")
    # nodes_sorted = sorted(s_graph.nodes())
    # list_nodes_str = [str(n) for n in nodes_sorted]
    # df_links = compute_similarities(s_graph, listofnodes=list_nodes_str)
    # print(df_links.head())
    
    # 8. Diffusion
    print("\n[8] Diffusion Model (ICM)...")
    # Random outbreak
    outbreak = random.sample(list(s_graph.nodes()), 5)
    infected = run_icm(s_graph, outbreak)
    print(f"Initial Outbreak: {len(outbreak)} nodes")
    print(f"Total Infected: {len(infected)} nodes")

if __name__ == "__main__":
    main()
