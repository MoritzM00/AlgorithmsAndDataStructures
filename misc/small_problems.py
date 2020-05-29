from typing import List


def get_min_max_rank(A: List[int], e: int) -> (int, int):
    """
    Given an array/list of integers, calculate the smallest and biggest possible rank of e.
    :param A: an iterable of integers
    :param e: an integer
    :return: (min, max)
    """
    min = -1
    max = -1
    rank = 0
    for x in A:
        if x < e:
            rank += 1
        elif x == e:
            if min == -1:
                min = rank
            if max == -1:
                max = rank
            else:
                max += 1
    return min, max


def test_min_max_rank():
    A = [1, 1, 2, 3, 3, 4]
    e = 3
    assert (3, 4) == get_min_max_rank(A, e)

    A = [1, 2, 2, 1, 1]
    assert (-1, -1) == get_min_max_rank(A, e)

    e = 1
    assert (0, 2) == get_min_max_rank(A, e)


if __name__ == '__main__':
    test_min_max_rank()
