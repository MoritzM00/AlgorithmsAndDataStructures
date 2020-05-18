from unittest import main, TestCase
from lists.doubly_linked_list import LinkedList, DoublyLinkedListNode


class DoublyLinkedListTestCase(TestCase):
    def test_basics(self):
        lst = LinkedList()
        with self.assertRaises(ValueError):
            lst.first()
        self.assertEqual(0, lst.size())

        lst = LinkedList([1, 2, 3, 4])
        self.assertEqual([1, 2, 3, 4], lst.to_array())
        self.assertFalse([1, 2, 3, 4] == lst)

    def test_insert(self):
        lst = LinkedList()
        for i in range(10):
            lst.push_back(i)

        self.assertEqual([i for i in range(10)], lst.to_array())

    def test_find(self):
        lst = LinkedList()
        n1 = DoublyLinkedListNode(1)

        lst._move_after(n1, lst.head)  # put n1 behind head

        self.assertEqual(n1, lst.find(1))

        self.assertIsNone(lst.find(2))

    def test_remove(self):
        lst = LinkedList([i for i in range(10)])
        lst.remove(lst.first())
        lst.remove(lst.last())

        self.assertEqual([i for i in range(1, 9)], lst.to_array())

    def test_concat(self):
        lst = LinkedList([1, 2, 3])
        other_lst = LinkedList([4, 5, 6])

        lst.concat(other_lst)

        self.assertEqual([1, 2, 3, 4, 5, 6], lst.to_array())

        lst.concat(LinkedList())

        self.assertEqual([1, 2, 3, 4, 5, 6], lst.to_array())

    def test_clear(self):
        lst = LinkedList([1, 2, 3])

        lst.clear()

        self.assertEqual([], lst.to_array())


if __name__ == '__main__':
    main()
