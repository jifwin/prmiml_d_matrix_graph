import networkx as nx
import matplotlib.pyplot as plt

NUMBER_OF_GRAPHS_OF_EACH_TYPE = 15
NUMBER_OF_NODES = 100
PROBABILITY_FACTOR = 0.15



def draw_graph(graph):
    nx.draw(graph)
    plt.show()


#todo: different parameters?
graphs = []

for i in xrange(NUMBER_OF_GRAPHS_OF_EACH_TYPE):
    graphs.append(nx.watts_strogatz_graph(NUMBER_OF_NODES, 2, PROBABILITY_FACTOR))
    graphs.append(nx.erdos_renyi_graph(NUMBER_OF_NODES, PROBABILITY_FACTOR))
    graphs.append(nx.barabasi_albert_graph(NUMBER_OF_NODES, 2))
    graphs.append(nx.powerlaw_cluster_graph(NUMBER_OF_NODES, 2, PROBABILITY_FACTOR))
