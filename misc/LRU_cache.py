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
        if self.cache.__contains__(key):
            self.cache.move_to_end(key)
        else:
            self.cache[key] = None
        self.num_entries += 1


def test_1():
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache.get(1))  # returns 1
    print(our_cache.get(2))  # returns 2
    print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print(our_cache.get(3))  # returns -1 because the cache reached its capacity


def test_2():
    cache = LRU_Cache()

    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)
    cache.set(1, 42)
    cache.set(5, 5)
    print(cache.get(1))  # should print 42 because of set command on line 91
    print(cache.get(2))  # should print -1
    cache.set(9, 90)  # 3 gets deleted now
    print(cache.get(3))  # should print -1


print('Test 1:')
test_1()
print('')
print('Test 2:')
test_2()
