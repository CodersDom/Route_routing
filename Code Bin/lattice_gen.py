import networkx as nx
import matplotlib.pyplot as plt

# 2 dimensional lattice graph
G_2_dim = nx.grid_2d_graph(4, 4)
# G_2_dim = nx.grid_2d_graph()

# n dimensional lattice graph
G_n_dim = nx.grid_graph(dim=[2, 3, 4])

# nx.draw('''The Graph to be Drawn''')
nx.draw(G_2_dim)

plt.show()
