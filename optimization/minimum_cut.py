def min_error(p, q, w: int, h: int) -> float:
    """
    Returns the minimum error between two 2D Arrays of [0, 1] with dimension w x h
    :param p: List of List of [0, 1]
    :param q: List of List of [0, 1]
    :param w: width of the array
    :param h: height of the array
    :return: minimum error: sum( (p_i,c(i) - q_i,c(i))^2 )
                with c(i) = { {0, ... , w-1}^h | for each i < h: |c_i - c_i-1| < 1}
    """
    # minimum error
    min_err = float("+inf")
    for j in range(w - 1):
        err = 0
        j_ = j
        for i in range(h):
            left = (p[i][j_ - 1] - q[i][j_ - 1]) ** 2
            mid = (p[i][j_] - q[i][j_]) ** 2
            right = (p[i][j_ + 1] - q[i][j_ + 1]) ** 2

            current_min = min(left, mid, right)
            err += current_min
            if current_min == left:
                j_ -= 1
            elif current_min == right:
                j_ += 1
        if err < min_err:
            min_err = err
    return min_err


def min_cut(p, q, w: int, h: int):
    """
    Returns the minimum cut between two 2D Arrays of [0, 1]
    :param p: List of List of [0, 1]
    :param q: List of List of [0, 1]
    :param w: width of the array
    :param h: height of the array
    :return: minimum cut between p and cut which minimizes the error defined above.
    """
    min_err = float("+inf")
    # minimum cut
    min_c = [-1 for _ in range(h)]

    for j in range(w - 1):
        err = 0
        c = [-1 for _ in range(h)]
        j_ = j
        for i in range(h):
            left = (p[i][j_ - 1] - q[i][j_ - 1]) ** 2
            mid = (p[i][j_] - q[i][j_]) ** 2
            right = (p[i][j_ + 1] - q[i][j_ + 1]) ** 2

            current_min = min(left, mid, right)
            err += current_min
            if current_min == left:
                c[i] = j_ - 1
                j_ -= 1
            elif current_min == mid:
                c[i] = j_
            else:
                c[i] = j_ + 1
                j_ += 1
        if err < min_err:
            min_err = err
            min_c = c

    return min_c
