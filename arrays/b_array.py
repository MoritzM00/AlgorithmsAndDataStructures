from typing import Iterable, Any, List


class BArray:
    """
    An BArray keeps track of its valid size. None Values are not allowed.
    """

    def __init__(self, data: List[int]):
        """
        An BArray is initialized with its initial size, containing None Values
        :param data: a list of ints
        """
        self.length = len(data)
        self.data = data

    def __repr__(self):
        return f"[{', '.join(map(str, self.data))}]"

    def get_data(self):
        return self.data[:self.length]

    def remove_value(self, value: Any):
        """
        Removing is done by setting the values to None and then closing the gaps by
        moving the other elements forward.
        Finally, the valid size of the array gets decreased by the number of elements which have been deleted.

        Runtime Analysis:
        Space: O(1)
        Time: - iterate over the array and set value to None O(n)
              - then close all gaps, which requires O(n) too
              -> O(n) time
        :param value: the value to remove
        """
        for i in range(self.length):
            if self.data[i] == value:
                self.data[i] = None
        self._close_gaps()

    def remove_indices(self, indices: Iterable[int]):
        """
        Removes all specified indices.

        Runtime Analysis:
        Space: O(1)
        Time: - O( len(indices) ) for deleting the indices
              - O(n) for closing the gaps
        :param indices: an iterable of ints
        """
        for index in indices:
            self.data[index] = None
        self._close_gaps()

    def _close_gaps(self):
        """
        Closes all gaps, which are identified by `None`
        and updates the length attribute
        """
        next = 0
        count = 0
        for i in range(self.length):
            if self.data[i] is not None:
                self.data[next] = self.data[i]
                next += 1
            else:
                count += 1
        self.length -= count
