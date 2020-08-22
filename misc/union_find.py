class UnionFind:
    """
    Union by rank data structures, which is used by Kruskals MST algorithm to efficiently
    identify different subtrees
    """

    def __init__(self, n: int):
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

        # invariant parent-refs lead to unique Partition-Representatives

    def find(self, i: int):
        assert i < self.n
        if self.parent[i] == i:
            return i
        else:
            j = self.find(self.parent[i])
            self.parent[i] = j  # compress path
            return j

    def union(self, i, j: int):
        x = self.find(i)
        y = self.find(j)
        if x != y:
            self.link(x, y)

    def link(self, i, j: int):
        # assert i and j are representatives of different blocks
        if self.rank[i] < self.rank[j]:
            self.parent[i] = j
        else:
            self.parent[j] = i
            if self.rank[i] == self.rank[j]:
                self.rank[i] += 1
