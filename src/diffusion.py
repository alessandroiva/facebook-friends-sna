import random
import matplotlib.pyplot as plt
import numpy as np

def run_icm(chosengraph, initialoutbreak, plot=False):
    """
    Independent Cascade Model (ICM) simulation.
    """
    activenodes = initialoutbreak[:]
    visited = initialoutbreak[:]
    next_activenodes = []
    t = 0
    n_visited = [len([x for x in chosengraph if x in visited])]
    n_notvisited = [len([x for x in chosengraph if x not in visited])]
    
    while activenodes:
        t = t + 1
        if len(activenodes) >= 2/3 * len(chosengraph):
            propagablenodes = random.sample(activenodes, round((1/3) * len(activenodes)))
            activenodes = propagablenodes[:]
            
        for node in activenodes:
            for neighbor in chosengraph[node]:
                if neighbor not in activenodes and neighbor not in visited:
                    not_visited_neighbors = 0
                    for n in chosengraph[neighbor]:
                        if n not in visited:
                            not_visited_neighbors += 1
                    
                    if len(chosengraph[neighbor]) > 0:
                        p = not_visited_neighbors / len(chosengraph[neighbor])
                    else:
                        p = 0
                        
                    if random.random() > p:
                        next_activenodes.append(neighbor)
                        visited.append(neighbor)
        
        n_visited.append(len([x for x in chosengraph if x in visited]))
        n_notvisited.append(len([x for x in chosengraph if x not in visited]))
        
        activenodes = next_activenodes[:]
        next_activenodes.clear()
    
    if plot:
        iterations = ['t=' + str(x) for x in range(t + 1)]
        x_axis = np.arange(len(iterations))
        plt.figure()
        plt.bar(x_axis - 0.2, n_notvisited, width=0.4, label='Not Activated')
        plt.bar(x_axis + 0.2, n_visited, width=0.4, label='Activated')
        plt.xticks(x_axis, iterations)
        plt.legend()
        plt.title("ICM Propagation")
        
    return visited
