from typing import Iterable, Any, List


class BArray:
    """
    An BArray keeps track of its valid size. None Values are not allowed.
    """

    def __init__(self, data: List[int]):
        self.length = len(data)
        self.data = data

    def __repr__(self):
        return f"[{', '.join(map(str, self.data))}]"

    def get_data(self):
        return self.data[:self.length]

    def remove_value(self, value: Any):
        """
        Removes all occurrences of this value.

        :param value: the value to remove
        """
        end = 0
        for i in range(self.length):
            self.data[end] = self.data[i]
            if self.data[i] != value:
                end += 1
        self.length = end

    def remove_indices(self, indices):
        """
        Removes all specified indices.

        :param indices: a sequence of ints
        """
        deleted = 0
        for i in range(self.length):
            self.data[i - deleted] = self.data[i]
            if deleted != len(indices) and indices[deleted] == i:
                deleted += 1
        self.length -= deleted
