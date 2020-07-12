import heapq


class MinPriorityQueue:
    def __init__(self, data):
        self.pq = data
        heapq.heapify(self.pq)

    def __sizeof__(self):
        return len(self.pq)

    def build(self, lst):
        """
        (Re-)Builds the priority queue
        :param lst:
        :return:
        """
        self.pq = lst
        heapq.heapify(self.pq)

    def insert(self, item):
        """
        Inserts the item.
        :param item: the inserted item
        :return: none
        """
        heapq.heappush(self.pq, item)

    def delete_min(self):
        """
        Deletes the minimum of the heap.
        :return: the minimum
        """
        return heapq.heappop(self.pq)

    def replace(self, item):
        """
        Pops the minimum of the heap and pushes the item onto int
        :param item: the pushed item
        :return: the minimum
        """
        return heapq.heapreplace(self.pq, item)

    def merge(self, *iterables, key=None, reverse=False):
        heapq.merge(self.pq, *iterables, key, reverse)

    def decrease_key(self, key):
        pass
