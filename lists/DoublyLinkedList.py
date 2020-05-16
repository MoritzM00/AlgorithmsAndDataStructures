class DoublyLinkedListNode:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    """
    Implementation of doubly linked list using a dummy header:
        Header.value == None
        Header.next == first element
        Header.prev == last element

    This implementation supports many O(1) time operations such
    as insertions, deletions and clearing at any given node in the list.
    Problem is that the size of the list cannot be returned in constant time
    because inter-list splice would otherwise not be in constant time.

    Free_list contains unused items and is used for deletion
    """

    def __init__(self):
        self.head = DoublyLinkedListNode()
        self.head.next = self.head
        self.head.prev = self.head

        self.free_list = LinkedList()

    def is_empty(self):
        return self.head.next == self.head

    def first(self):
        if self.is_empty():
            raise ValueError("empty list")
        return self.head.next

    def last(self):
        if self.is_empty():
            raise ValueError("empty list")
        return self.head.prev

    def splice(self, a, b, t):
        """
        Cuts out the sublist from a to b and insert after t.
        :param a: from
        :param b: to
        :param t: insert after t
        :return: None
        """
        # assert b is not before a and t is not in <a....b>

        # cut out from a to b
        a_ = a.next
        b_ = b.prev

        a_.next = b_
        b_.prev = a_

        # insert a....b after t
        t_ = t.next

        b.next = t_
        a.prev = t

        t.next = a
        t_.prev = b

    def move_after(self, some_node, after):
        """
        Moves some_node behind the node after
        :param some_node: some node in the list
        :param after: the node where some_node is added
        :return: None
        """
        self.splice(some_node, some_node, after)

    def move_to_front(self, node):
        """
        Moves the given node to the front of the list.
        :param node: the new front of the list
        :return: None
        """
        self.move_after(node, self.head)

    def move_to_back(self, node):
        """
        Moves the given node to the back of the list.

        :param node: the new tail of the list
        :return: None
        """
        self.move_after(node, self.head.prev)

    def remove(self, node):
        """
        Removes the given node.
        :param node: the node to remove
        :return: None
        """
        self.move_after(node, self.free_list.head)

    def pop_front(self):
        """
        Pops off the front element.
        :return: None
        """
        assert not self.is_empty()
        self.remove(self.head.next)

    def pop_back(self):
        """
        Pop off the tail
        :return: None
        """
        assert not self.is_empty()
        self.remove(self.head.prev)

    def insert_after(self, value, node):
        """
        Inserts the given value after the given node.
        :param value: the value to insert
        :param node: value gets placed after this node
        :return: the new node
        """
        assert self.free_list.is_empty()  # make sure free list is empty
        a_ = self.free_list.first()  # obtain an item a_ to hold value
        self.move_after(a_, node)  # put it to the right place
        a_.value = value  # and fill it with the right content
        return a_

    def insert_before(self, value, node):
        """
        Inserts the given value before the given node.
        :param value: the value to insert
        :param node: value gets placed before this node
        :return: the new node
        """
        return self.insert_after(value, node.prev)

    def push_front(self, value):
        """
        Pushes the given value to the head of the list
        :param value: the new head
        :return: None
        """
        self.insert_after(value, self.head)

    def push_back(self, value):
        """
        Pushes the given value to the tail of the list
        :param value: the new tail
        :return: None
        """
        self.insert_after(value, self.head.prev)

    def concat(self, other_list):
        """
        Concatenates this list with other_list
        :param other_list: the list to concatenate
        :return: None
        """
        self.splice(other_list.first(),
                    other_list.last(),
                    self.head.prev)

    def clear_all(self):
        """
        Clears the list in constant time.

        :return: None
        """
        self.free_list.concat(self)

    def find_next(self, value, from_):
        # sentinel
        self.head.value = value
        while from_.next != value:
            from_ = from_.next
        return from_
