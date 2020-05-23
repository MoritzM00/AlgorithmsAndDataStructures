from typing import List
from collections import namedtuple
from random import randint
import numpy as np

Screw = namedtuple('Screw', 'length diameter')


def count_screws(screws: List[Screw]) -> List[List[int]]:
    """
    A Screw Type consists of the length and the diameter of the screw.
    Calculates the amount of screw types which occur.
    :param screws: A list of screws
    :return: An 2D Array, where the row index is the length,
     and the column index is the diameter of the screw.
    """
    max_length = max(screws, key=lambda x: x.length).length
    max_diameter = max(screws, key=lambda x: x.diameter).diameter
    min_length = min(screws, key=lambda x: x.length).length
    min_diameter = min(screws, key=lambda x: x.diameter).diameter

    diff_length = max_length - min_length
    diff_diameter = max_diameter - min_diameter

    counts = [[0 for col in range(diff_diameter + 1)] for row in range(diff_length + 1)]

    for screw in screws:
        i = screw.length - min_length
        j = screw.diameter - min_diameter
        counts[i][j] += 1

    return counts


def test():
    screws = [Screw(i % 2, (i + 1) % 2) for i in range(30)]
    screws.extend([Screw(randint(0, 4), randint(0, 4)) for _ in range(100)])
    print(np.array(count_screws(screws)))


if __name__ == '__main__':
    test()
