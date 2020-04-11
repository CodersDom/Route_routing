import packet
import RandomGen
import ProbabilityFunction
import dijkstra



send_packet = RandomGen.ReturnRandom(16)

src = send_packet[0]
dest = send_packet[1]

matrix = []

edgeslist = ProbabilityFunction.matrixEdges(matrix, ProbabilityFunction.n)

print(edgeslist)


graph = dijkstra.Graph(ProbabilityFunction.n * ProbabilityFunction.n)
# graph = Graph()
print("The Graph is (Src , Destination , weight)")
for i in edgeslist:
    # graph.add_edge(i)
    u = i["pt1"]
    v = i["pt2"]
    w = i["weight"]
    print(u, v, w)
    graph.addEdge(u, v, w)

# packet.send()
# packet.recieve()
# for loss track the recieved and '-' it for the send_packet.

print("Shortest Path between %d and %d is " % (src, dest)),
l = graph.findShortestPath(src, dest)

print("\nShortest Distance between %d and %d is %d " % (src, dest, l)),
