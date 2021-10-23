class Graph:
    def __init__(self, n: int):
        """
        Initiates the graph of vertex count n
        :param n: vertex count
        """
        self.vertex_count = n
        self.m = [[0 for col in range(n)] for row in range(n)]

    def num_connectivity(self):
        """
        Finds the number of connected components in this graph
        :return: the number of connected components
        """
        n = 0
        marked = [False for _ in range(self.vertex_count)]
        while True:
            # find next unmarked vertex
            v = -1
            for i in range(self.vertex_count):
                if not marked[i]:
                    v = i
                    break
            if v == -1:
                break

            # if we found another vertex, then we have another
            # connected component
            n += 1

            # run DFS, that marks all vertex that are reachable from v
            s = [v]
            while not len(s) == 0:
                v = s.pop()
                marked[v] = True
                for u in range(self.vertex_count):
                    if self.m[v][u]:
                        s.append(u)
