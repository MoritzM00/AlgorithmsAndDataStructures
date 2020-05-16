from typing import Any


class DoublyLinkedListNode:
    def __init__(self, value: Any = None):
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
    as insertions, concatenation, deletions and clearing at any given node in the list.
    Problem is that the size of the list cannot be returned in constant time
    because inter-list splice would otherwise not be in constant time.

    Free_list contains unused items and is used for deletion
    """

    def __init__(self):
        self.head = DoublyLinkedListNode()
        self.head.next = self.head
        self.head.prev = self.head

        self.free_list = LinkedList()

    def is_empty(self) -> bool:
        """
        Returns true if the list is emtpy.

        :return: true if list is empty
        """
        return self.head.next == self.head

    def first(self) -> DoublyLinkedListNode:
        """
        Returns the first element in the list
        :return: the first element
        """
        if self.is_empty():
            raise ValueError("empty list")
        return self.head.next

    def last(self) -> DoublyLinkedListNode:
        """
        Returns the last element in the list
        :return: the last element
        """
        if self.is_empty():
            raise ValueError("empty list")
        return self.head.prev

    def splice(self, a: DoublyLinkedListNode,
               b: DoublyLinkedListNode,
               t: DoublyLinkedListNode) \
            -> None:
        """
        Cuts out the sublist from a to b and insert after t.
        :param a: from
        :param b: to
        :param t: insert after t
        :return: None
        """
        # assert b is not before a and t is not in <a....b>
        if self.is_empty():
            raise ValueError("empty list")
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

    def move_after(self, some_node: DoublyLinkedListNode,
                   after: DoublyLinkedListNode) \
            -> None:
        """
        Moves some_node behind the node after
        :param some_node: some node in the list
        :param after: the node where some_node is added
        :return: None
        """
        self.splice(some_node, some_node, after)

    def move_to_front(self, node: DoublyLinkedListNode) -> None:
        """
        Moves the given node to the front of the list.
        :param node: the new front of the list
        :return: None
        """
        self.move_after(node, self.head)

    def move_to_back(self, node: DoublyLinkedListNode) -> None:
        """
        Moves the given node to the back of the list.

        :param node: the new tail of the list
        :return: None
        """
        self.move_after(node, self.head.prev)

    def remove(self, node: DoublyLinkedListNode) -> None:
        """
        Removes the given node.
        :param node: the node to remove
        :return: None
        """
        self.move_after(node, self.free_list.head)

    def pop_front(self) -> None:
        """
        Pops off the front element.
        :return: None
        """
        self.remove(self.first())

    def pop_back(self) -> None:
        """
        Pop off the tail
        :return: None
        """
        self.remove(self.last())

    def insert_after(self, value: Any, node: DoublyLinkedListNode) \
            -> DoublyLinkedListNode:
        """
        Inserts the given value after the given node.
        :param value: the value to insert
        :param node: value gets placed after this node
        :return: the new node
        """
        assert not self.free_list.is_empty()  # make sure free list is non-empty
        a_ = self.free_list.first()  # obtain an item a_ to hold value
        self.move_after(a_, node)  # put it to the right place
        a_.value = value  # and fill it with the right content
        return a_

    def insert_before(self, value: Any, node: DoublyLinkedListNode) \
            -> DoublyLinkedListNode:
        """
        Inserts the given value before the given node.
        :param value: the value to insert
        :param node: value gets placed before this node
        :return: the new node
        """
        return self.insert_after(value, node.prev)

    def push_front(self, value: Any) -> None:
        """
        Pushes the given value to the head of the list
        :param value: the new head
        :return: None
        """
        self.insert_after(value, self.head)

    def push_back(self, value: Any) -> None:
        """
        Pushes the given value to the tail of the list
        :param value: the new tail
        :return: None
        """
        self.insert_after(value, self.last())

    def concat(self, other_list) -> None:
        """
        Concatenates this list with other_list
        :type other_list: LinkedList
        :param other_list: the list to concatenate
        :return: None
        """
        self.splice(other_list.first(),
                    other_list.last(),
                    self.last())

    def clear_all(self) -> None:
        """
        Clears the list in constant time.

        :return: None
        """
        self.free_list.concat(self)

    def find_next(self, value: Any, from_: DoublyLinkedListNode) \
            -> DoublyLinkedListNode:
        # sentinel
        self.head.value = value
        while from_.next != value:
            from_ = from_.next
        return from_

    def size(self) -> int:
        """
        Calculates the size of the list in !! linear time !!
        :return: the size of the list
        """
        size = 0
        if self.is_empty():
            return size
        current = self.first()
        while current:
            size += 1
            current = current.next
        return size

    def __repr__(self) -> str:
        if self.is_empty():
            return "[]"

        current = self.first()
        result = "["
        while current:
            result += str(current.value)
            result += ", "
            current = current.next
        result[:-2]
        result += "]"
        return result
