import random
from joblib import Parallel, delayed
import networkx as nx
import numpy as np
from networkx import shortest_path

NUMBER_OF_GRAPHS_OF_EACH_TYPE = 10
NUMBER_OF_NODES = 1000
PROBABILITY_FACTORS = np.linspace(0.05,0.1,3)
M_OR_K_PARAMS = [4,5]

graphs = []

for i in xrange(NUMBER_OF_GRAPHS_OF_EACH_TYPE):
    graphs.append(nx.connected_watts_strogatz_graph(NUMBER_OF_NODES, random.choice(M_OR_K_PARAMS), random.choice(PROBABILITY_FACTORS)))
    graphs.append(nx.erdos_renyi_graph(NUMBER_OF_NODES, random.choice(PROBABILITY_FACTORS)))
    graphs.append(nx.barabasi_albert_graph(NUMBER_OF_NODES, random.choice(M_OR_K_PARAMS)))
    graphs.append(nx.powerlaw_cluster_graph(NUMBER_OF_NODES, random.choice(M_OR_K_PARAMS), random.choice(PROBABILITY_FACTORS)))

max_diameter = max([nx.diameter(graph) for graph in graphs])

def calculate_b_matrix(graph):
    print graph
    b_matrix = np.zeros((max_diameter, NUMBER_OF_NODES))

    for source_node in graph.nodes():
        path = shortest_path(graph, source_node)
        path.pop(source_node)
        distances = {key: len(values) for (key, values) in path.iteritems()}
        for (l, k) in distances.iteritems():
            b_matrix[k-2, l] += 1

    return b_matrix.flatten()


results = Parallel(n_jobs=8)(delayed(calculate_b_matrix)(graph) for graph in graphs)
np.save("results.bin", results)
