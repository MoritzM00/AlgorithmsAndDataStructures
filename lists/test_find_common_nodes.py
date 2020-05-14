from unittest import TestCase, main

from lists.find_common_nodes import has_common_node, find_first_common_node
from lists.node import Node


class FindCommonNodesTestCase(TestCase):
    n1 = None
    n2 = None
    b = None

    def setUp(self) -> None:
        self.n1 = Node("n1")
        a = Node("a")
        self.b = Node("b")
        c = Node("c")

        self.n2 = Node("n2")
        self.d = Node("d")

        self.n1.next = a
        a.next = self.b
        self.b.next = c

        self.n2.next = self.d
        self.d.next = self.b

        # List 1: n1 -> a -> b -> c -> None
        #                       ^
        # List 2: n2 -> d -> b  |
        # so b is the first common node to find here

    def test_has_common_node(self):
        self.assertTrue(has_common_node(self.n1, self.n2))
        self.assertEqual(find_first_common_node(self.n1, self.n2), self.b)


if __name__ == '__main__':
    main()
