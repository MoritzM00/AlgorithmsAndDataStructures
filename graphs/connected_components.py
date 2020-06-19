from collections import deque


class Graph:
    def __init__(self, n: int):
        """
        Initiates the graph of vertex count n
        :param n: vertex count
        """
        self.vertexCount = n
        self.m = [[0 for col in range(n)] for row in range(n)]

    def max_connected_components(self):
        return max(
            [self.find_connected_components(vertex) for vertex in range(self.vertexCount)]
        )

    def find_connected_components(self, start_vertex: int):
        """
        Returns the number of connected components of this graph
        :param start_vertex: the starting point of the modified BFS algorithm
        :return: number of connected components for this start vertex
        """
        components = 1
        markers = [False for _ in range(self.vertexCount)]
        q = deque()
        q.append(start_vertex)
        markers[start_vertex] = True

        while not len(q) == 0:
            current = q.pop()
            for i in range(self.vertexCount):
                if self.m[current][i] and not markers[i]:
                    markers[i] = True
                    q.append(i)
                    components += 1

        return components
