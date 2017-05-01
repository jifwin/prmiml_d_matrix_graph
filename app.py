import networkx as nx
import matplotlib.pyplot as plt

NUMBER_OF_NODES = 100
PROBABILITY_FACTOR = 0.15


def draw_graph(graph):
    nx.draw(graph)
    plt.show()

#todo: different parameters?

graph1 = nx.watts_strogatz_graph(NUMBER_OF_NODES, 2, PROBABILITY_FACTOR)
draw_graph(graph1)
graph2 = nx.erdos_renyi_graph(NUMBER_OF_NODES, PROBABILITY_FACTOR)
draw_graph(graph2)
graph3 = nx.barabasi_albert_graph(NUMBER_OF_NODES, 2)
draw_graph(graph3)
graph4 = nx.powerlaw_cluster_graph(NUMBER_OF_NODES, 2, PROBABILITY_FACTOR)
draw_graph(graph4)