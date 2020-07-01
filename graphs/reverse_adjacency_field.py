def reverse_adj_field(n, offsets, edges):
    """
    Reverses the an adjacency field graph
    :param n: number of vertices
    :param offset: a list which contains the start index of the vertex i at offset[i]
                in the edges list
    :param edges: a list containing the vertices. Offet determines, which edge is meant
    :return: the new offset and edges list for the reversed graph
    """
    # calculate indegree of each vertex
    incident = [0 for _ in range(n)]
    for v in edges:
        incident[v] += 1

    # prefix sum of indegrees is offset for the new graph
    offsets_ = [0 for _ in range(n + 1)]
    for i in range(len(incident)):
        offsets_[i + 1] = offsets_[i] + incident[i]
        incident[i] = 0

    # determine indices of the new adjacency field
    edges_ = [0 for _ in range(edges)]
    for i in range(n):
        # the edges corresponding to i start at offsets_[i]
        j = offsets_[i]
        # and run until offsets_[i + 1]
        while j < offsets_[i + 1]:
            to = edges[j]
            edges_[offsets_[to] + incident[to]] = i
            incident[to] += 1
    return offsets_, edges_
