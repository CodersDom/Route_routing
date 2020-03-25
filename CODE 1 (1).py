import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.nodes(), G.edges()
for i in range(1, 13):
    G.add_node(i)
G.nodes()

print("number of nodes in the graph :", G.number_of_nodes())

G.add_edges_from(
    [
        (1, 2),
        (1, 4),
        (2, 3),
        (2, 5),
        (3, 6),
        (4, 5),
        (4, 7),
        (5, 6),
        (5, 8),
        (6, 9),
        (7, 8),
        (7, 10),
        (8, 9),
        (8, 11),
        (9, 12),
        (10, 11),
        (11, 12),
    ]
)

print(G.nodes())
print("number of edges in the graph:", G.number_of_edges())
print("edges in the graph:", G.edges())
print("degree counts per node:", G.degree())

G.neighbors(1)

nx.draw_networkx(G, with_labels=True)
plt.show()


path = nx.shortest_path(G, source=1, target=11)
print(path)
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color="k", with_labels=True)
path_edges = list(zip(path, path[1:]))
nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="r")
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="r", width=10)
plt.axis("equal")
plt.show()
