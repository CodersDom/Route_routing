import networkx as nx

import matplotlib.pyplot as plt

G = nx.path_graph(5)
print(nx.shortest_path(G, source=0, target=4))

p = nx.shortest_path(G, source=0)  # target not specified

p = nx.shortest_path(G, target=4)  # source not specified

p = nx.shortest_path(G)  # source, target not specified


nx.draw_networkx(p, with_labels=True)
plt.show()
