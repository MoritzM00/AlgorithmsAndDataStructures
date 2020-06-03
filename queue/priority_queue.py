from sorting.quick_select import swap


class MinPriorityQueue:
    """
    Implements a min priority queue with a binary heap.
    """

    def __init__(self):
        self.n = 0
        self.h = []

    def __sizeof__(self):
        return len(self.h)

    def insert(self, e):
        """
        Inserts the given number into the priority queue in O(log n)
        :param e: a number
        :return: None
        """
        self.n += 1
        self.h.append(e)
        self._up_heapify(self.n)

    def _up_heapify(self, i: int):
        """
        Makes sure that the min-heap priority is not violated
        :param i:
        :return:
        """
        # assert: the heap property holds except maybe at position i
        if i == 1 or self.h[i // 2] <= self.h[i]:
            return
        else:
            swap(self.h, i // 2, i)

            self._up_heapify(i // 2)

    def delete_min(self):
        """
        Returns the minimum and deletes it in O(log n)
        :return: the minimum
        """
        result = self.h[0]
        self.h[0] = self.h[self.n]
        self.n -= 1
        self._down_heapify(1)
        return result

    def _down_heapify(self, i: int):
        """
        Makes sure that the min-heap property is not violated.
        Runtime: O(log n) time
        :param i: the index in the heap
        :return: None
        """
        # assert heap property except possibly at j = 2i and j = 2i + 1

        # if node i has children, then
        if 2 * i <= self.n:
            m: int
            # if there is no right child
            # or if the left one is smaller than the right child
            if 2 * i + 1 > self.n \
                    or self.h[2 * i] <= self.h[2 * i + 1]:
                # select left child
                m = 2 * i
            else:
                # select the second/right children
                m = 2 * i + 1

            if self.h[i] > self.h[m]:  # heap property violated
                swap(self.h, i, m)
                self._down_heapify(m)

        # assert heap property holds for the subtree rooted at i
