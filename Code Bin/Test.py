import matplotlib.pyplot as plt
import networkx as nx

import ProbabilityFunction
import dijkstra1

matrix = []

edgeslist = ProbabilityFunction.matrixEdges(matrix, ProbabilityFunction.n)

# print(edgeslist)

G = nx.Graph()

graph = dijkstra1.Graph(ProbabilityFunction.n * ProbabilityFunction.n)
for i in edgeslist:
    # graph.add_edge(i)
    u = i["pt1"]
    v = i["pt2"]
    w = i["weight"]
    print(u, v, w)
    G.add_edge(u, v, weight=w)

print("The Graph is ")
# graph.show_graph()
# graph.dijkstra(1)

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]
pos = nx.spring_layout(G)  # positions for all nodes
# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(
    G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
)

# labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

plt.axis("off")
plt.show()
