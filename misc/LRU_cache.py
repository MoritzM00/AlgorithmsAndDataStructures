from collections import OrderedDict


class LRU_Cache(object):
    """
    Implements a Least Recently Used (LRU) Cache with an Ordered Dictionary.
    """

    def __init__(self, capacity=5):
        # an ordered dict keeps track of the order of insertions in contrast to a normal dict
        # which does not keep the order
        self.cache = OrderedDict()
        self.capacity = capacity
        self.num_entries = 0

    def is_full(self):
        """
        Returns true if the cache is full
        :return: true if the cache is full
        """
        return self.capacity == self.num_entries

    def del_lru_item(self):
        """
        Deletes the least recently used item.

        :return: None
        """
        # pops and deletes the least recently used key, which is at the
        # beginning of the ordered dict
        self.cache.popitem(last=False)
        self.num_entries -= 1

    def get(self, key):
        """
        Retrieve item from provided key. Return -1 if nonexistent.

        :param key: the key of the value
        :return: the value if present, -1 otherwise
        """
        value = self.cache.get(key)
        if not value:
            return -1
        else:
            # move the key to the end of the order
            self.cache.move_to_end(key)  # O(1)
            return value

    def set(self, key, value):
        """
        Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        :param key: the key of the value
        :param value: the new value
        :return:
        """
        if self.is_full():
            # remove oldest item
            self.del_lru_item()
        self.cache[key] = value
        if key in self.cache:
            self.cache.move_to_end(key)
        else:
            self.cache[key] = None
        self.num_entries += 1
