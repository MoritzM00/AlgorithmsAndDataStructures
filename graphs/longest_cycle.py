from collections import deque


def longest_cyle(v, vertices, edges):
    """
    Finds the longest cycle in the graph, that contains the vertex u
    :param v: the vertex v
    :param vertices: list of vertexes
    :param edges: edge list (u,v) for u,v element of V
    :return: the length of the longest cycle containing u
    """
    queue = deque()
    queue.append(v)
    l = [0 for _ in range(len(vertices))]
    length = 0
    depth = 0
    while not len(queue) == 0:
        x = queue.popleft()
        depth = l[x] + 1
        edges_ = [(u, v) for (u, v) in edges if u == x]
        for (a, b) in edges_:
            if b == v or l[b] > 0:
                length = max(length, depth + l[b])
            else:
                queue.append(b)
                l[b] = depth
    return length
