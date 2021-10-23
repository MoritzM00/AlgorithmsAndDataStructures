from unittest import TestCase, main
from misc.LRU_cache import LRU_Cache


class LRUTestCase(TestCase):
    def test_get(self):
        cache = LRU_Cache(5)

        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)

        self.assertEqual(1, cache.get(1))
        self.assertEqual(2, cache.get(2))
        self.assertEqual(-1, cache.get(9))  # returns -1 because 9 is not present in the cache

        cache.set(5, 5)
        cache.set(6, 6)

        self.assertEqual(-1, cache.get(3))  # returns -1 because the cache reached its capacity

    def test_lru_gets_deleted(self):
        cache = LRU_Cache()

        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)
        cache.set(1, 42)
        cache.set(5, 5)

        self.assertEqual(42, cache.get(1))

        self.assertEqual(-1, cache.get(2))
        cache.set(9, 90)  # 3 gets deleted now

        self.assertEqual(-1, cache.get(3))


if __name__ == '__main__':
    main()
