import networkx as nx

def custom_pagerank(g, alpha=0.85):
    """
    Custom PageRank implementation.
    """
    g = nx.DiGraph(g)
    outlinks = {}
    inlinks = {}
    listof_edges = nx.edges(g)
    
    for i in listof_edges:
        if i[0] not in outlinks:
            outlinks[i[0]] = [i[1]]
        else:
            outlinks[i[0]].append(i[1])
        if i[1] not in inlinks:
            inlinks[i[1]] = [i[0]]
        else:
            inlinks[i[1]].append(i[0])
            
    # Logic to handle nodes with no outgoing edges within the sub-context if any
    for n in g.nodes():
        if n not in outlinks: outlinks[n] = []
        if n not in inlinks: inlinks[n] = []

    rt = {n: (1 / (len(nx.nodes(g)))) for n in g}
    times = 0
    while True:
        prev_rt = rt.copy()
        for n in prev_rt:
            result = 0
            for i in inlinks[n]:
                numerator = prev_rt[i]
                denominator = len(outlinks[i])
                if denominator == 0:
                    result += 0 
                else:
                    result += (numerator / denominator)
            rt[n] = result
            
        for n in rt:
            rt[n] = (1 - alpha) / len(g) + alpha * rt[n] 
            
        times += 1
        if list(prev_rt.values()) == list(rt.values()) or times > 100: 
            return rt, times
