import networkx as nx
import numpy as np
import collections

from networkx import shortest_path
import matplotlib.pyplot as plt

NUMBER_OF_GRAPHS_OF_EACH_TYPE = 50
NUMBER_OF_NODES = 1000
PROBABILITY_FACTOR = 0.15



def draw_graph(graph):
    nx.draw(graph)
    plt.show()


#todo: different parameters?
graphs = []

for i in xrange(NUMBER_OF_GRAPHS_OF_EACH_TYPE):
    graphs.append(nx.connected_watts_strogatz_graph(NUMBER_OF_NODES, 2, PROBABILITY_FACTOR))
    graphs.append(nx.erdos_renyi_graph(NUMBER_OF_NODES, PROBABILITY_FACTOR))
    graphs.append(nx.barabasi_albert_graph(NUMBER_OF_NODES, 2))
    graphs.append(nx.powerlaw_cluster_graph(NUMBER_OF_NODES, 2, PROBABILITY_FACTOR))

b_matrices = []
i = 0
for graph in graphs:
    print i #todo: just for debug
    nodes = graph.nodes()
    b_matrix = np.zeros((NUMBER_OF_NODES, NUMBER_OF_NODES))

    for source_node in graph.nodes():
        path = shortest_path(graph, source_node)
        path.pop(source_node)
        distances = [len(path[key]) for key in path.keys()]
        for (l, k) in collections.Counter(distances).iteritems():
            b_matrix[k,l] += 1

    b_matrices.append(b_matrix)
    i += 1