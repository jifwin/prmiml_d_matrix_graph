from joblib import Parallel, delayed
import networkx as nx
import numpy as np
import collections
import uuid

from networkx import shortest_path

NUMBER_OF_GRAPHS_OF_EACH_TYPE = 12
NUMBER_OF_NODES = 1000
PROBABILITY_FACTOR = 0.15

# todo: different parameters?
graphs = []

for i in xrange(NUMBER_OF_GRAPHS_OF_EACH_TYPE):
    graphs.append(nx.connected_watts_strogatz_graph(NUMBER_OF_NODES, 2, PROBABILITY_FACTOR))
    graphs.append(nx.erdos_renyi_graph(NUMBER_OF_NODES, PROBABILITY_FACTOR))
    graphs.append(nx.barabasi_albert_graph(NUMBER_OF_NODES, 2))
    graphs.append(nx.powerlaw_cluster_graph(NUMBER_OF_NODES, 2, PROBABILITY_FACTOR))


def calculate_b_matrix(graph):
    print graph
    b_matrix = np.zeros((NUMBER_OF_NODES, NUMBER_OF_NODES))

    for source_node in graph.nodes():
        path = shortest_path(graph, source_node)
        path.pop(source_node)
        distances = [len(path[key]) for key in path.keys()]
        for (l, k) in collections.Counter(distances).iteritems():
            b_matrix[k, l] += 1

    return b_matrix.flatten()


results = Parallel(n_jobs=8)(delayed(calculate_b_matrix)(graph) for graph in graphs)
np.save("results.bin", results)
