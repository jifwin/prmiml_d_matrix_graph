import networkx as nx
import matplotlib.pyplot as plt

NUMBER_OF_NODES = 1000

watts_strogatz = nx.watts_strogatz_graph(NUMBER_OF_NODES,2,0.15)

nx.draw(watts_strogatz)
plt.show()