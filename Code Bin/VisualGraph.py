class Packets:
    def __init__(self):
        self.PathList = {}  # To store graph: u -> (v,w)nodes to covered
        self.coveredNodeList = {}  # To store covered node no


class Graph:
    class _Node:
        __slots__ = "_w", "_x", "_y", "_z", "_destination", "_packet_queue"

        def __init__(
            self, w=None, x=None, y=None, z=None, destination=None, packet_queue=[]
        ):
            self._w = w
            self._x = x
            self._y = y
            self._z = z
            self._destination = destination
            self._packet_queue = []

        def _getallNodeAttributes(self):
            return (self._w, self._x, self._y, self._z)

        def _updateWProbability(self, W):
            self._w = W
            return (self._w, self._x, self._y, self._z)

        def _updateXProbability(self, X):
            self._x = X
            return (self._w, self._x, self._y, self._z)

        def _updateYProbability(self, Y):
            self._y = Y
            return (self._w, self._x, self._y, self._z)

        def _updateZProbability(self, Z):
            self._z = Z
            return (self._w, self._x, self._y, self._z)

    # ,_data=None,_size=None,_font=None,_sourcepos=None,_destination=None
    _size = 0

    def __init__(self):
        self._data = []

    def _addNode(self, w, x, y, z):
        # if (self._size)==len(self._data):
        #     self._resize(2*len(self.data))
        # avail = (self._font + self._size)%len(self._data)
        # avail = self._size
        self._data.append(
            self._Node(w, x, y, z, None, [1, 2, 5, 8, 11])
        )  # Destination = NOne and stack is empty
        self._size += 1

    def _getLength(self):
        return self._size

    def _getFirst(self):
        return self._data[0]

    def _getAllNodes(self):
        for i in range(self._size):
            print(self._data[i]._getallNodeAttributes())

    def _updateWProbability(self, nodeno, W):
        return self._data[nodeno - 1]._updateWProbability(W)

    def _updateXProbability(self, nodeno, X):
        return self._data[nodeno - 1]._updateXProbability(X)

    def _updateYProbability(self, nodeno, Y):
        return self._data[nodeno - 1]._updateYProbability(Y)

    def _updateZProbability(self, nodeno, Z):
        return self._data[nodeno - 1]._updateZProbability(Z)


G = Graph()
G._addNode(1, 1, 1, 1)

G._addNode(1, 1, 1, 1)

print(G._getLength())
print(G._getAllNodes())

G._updateWProbability(1, 2)
G._updateXProbability(1, 2)
G._updateYProbability(1, 2)
G._updateZProbability(1, 2)

print(G._getAllNodes())
