from typing import NamedTuple, List


class Screw(NamedTuple):
    """
    A screw type consists of the length, the diameter and the number of coils.
    """
    length: int
    diameter: int
    coils: int


def count_screws(screws: List[Screw]) -> List[List[int]]:
    pass
