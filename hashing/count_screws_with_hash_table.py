from typing import NamedTuple, List, Dict
from random import randint
from pprint import pprint


class Screw(NamedTuple):
    """
    A screw type consists of the length, the diameter and the number of coils.
    """
    length: int
    diameter: int
    coils: int


def count_screws(screws: List[Screw]) -> Dict[Screw, int]:
    """
    Counts the number of each screw type.

    :param screws: a list of screws
    :return: a dict containing the number of screws per type
    """
    counts = {}
    for screw in screws:
        if screw in counts:
            counts[screw] += 1
        else:
            counts[screw] = 1
    return counts


def test():
    screws = [Screw(i % 2, (i + 1) % 2, (i * 3) % 2) for i in range(30)]
    screws.extend(
        [Screw(randint(0, 3), randint(0, 3), randint(0, 3)) for _ in range(100)])
    pprint(count_screws(screws))


if __name__ == '__main__':
    test()
