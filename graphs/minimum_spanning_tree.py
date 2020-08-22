from misc.union_find import UnionFind
from typing import NamedTuple, List
from operator import attrgetter


class Edge(NamedTuple):
    """
    An Edge has a start and end vertex (represented by ints), as well as a weight.
    """
    start: int
    end: int
    weight: float


def kruskal(edges: List[Edge], n):
    edges = sorted(edges, key=attrgetter('weight'))
    Tc = UnionFind(n)
    for start, end, weight in edges:
        if Tc.find(start) != Tc.find(end):
            Tc.link(start, end)
        # or simply Tc.union(start, end)
    # return MST
