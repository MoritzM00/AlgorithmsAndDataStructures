from typing import Any, List


class DoublyLinkedListNode:
    def __init__(self, value: Any = None, is_dummy: bool = False):
        """
        Creates a DoublyLinkedListNode with the specified value.
        If is_dummy is True, then this node will have pointers prev and next to itself instead of None
        :param value: the value
        :param is_dummy: true if this node is a dummy
        """
        self.value = value
        if is_dummy:
            self.prev = self
            self.next = self
        else:
            self.prev = None
            self.next = None

    def __repr__(self):
        return "node: " + str(self.value)


class LinkedList:
    """
    Implementation of doubly linked list using a dummy header:
        Header.value == None
        Header.next == first element
        Header.prev == last element

    This implementation supports many O(1) time operations such
    as insertions, concatenation, deletions and clearing at any given node in the list.
    Problem is that the size of the list cannot be returned in constant time
    because inter-list _splice would otherwise not be in constant time.

    """

    def __init__(self, data=None):
        self.head = DoublyLinkedListNode(is_dummy=True)

        if data:
            self.from_iterable(data)

    def __iter__(self):
        current = self.head.next

        while current is not self.head:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self.size()

    def __repr__(self) -> str:
        return f"[{', '.join([str(x) for x in self])}]"

    def __eq__(self, other):
        if isinstance(other, LinkedList):
            this = self.head
            other_ = other.head
            while this.next is not self.head \
                    and other_.next is not other.head:
                if this.value != other_.value:
                    return False
            return True
        return False

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

    def _splice(self, a: DoublyLinkedListNode,
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

        # cut out from a to b
        a_ = a.prev
        b_ = b.next

        if a_:
            a_.next = b_
        if b_:
            b_.prev = a_

        # insert a....b after t
        t_ = t.next

        b.next = t_
        a.prev = t

        t.next = a
        t_.prev = b

    def _move_after(self, some_node: DoublyLinkedListNode,
                    after: DoublyLinkedListNode) \
            -> None:
        """
        Moves some_node behind the node after
        :param some_node: some node in the list
        :param after: the node where some_node is added
        :return: None
        """
        self._splice(some_node, some_node, after)

    def _move_to_front(self, node: DoublyLinkedListNode) -> None:
        """
        Moves the given node to the front of the list.
        :param node: the new front of the list
        :return: None
        """
        self._move_after(node, self.head)

    def _move_to_back(self, node: DoublyLinkedListNode) -> None:
        """
        Moves the given node to the back of the list.

        :param node: the new tail of the list
        :return: None
        """
        self._move_after(node, self.head.prev)

    def remove(self, node: DoublyLinkedListNode) -> None:
        """
        Removes the given node.
        :param node: the node to remove
        :return: None
        """
        trash = DoublyLinkedListNode(is_dummy=True)
        self._move_after(node, trash)
        del trash

    def pop_front(self) -> None:
        """
        Pops off the front element.
        :return: None
        """
        self.remove(self.head.next)

    def pop_back(self) -> None:
        """
        Pop off the tail
        :return: None
        """
        self.remove(self.head.prev)

    def _insert_after(self, value: Any, node: DoublyLinkedListNode) \
            -> DoublyLinkedListNode:
        """
        Inserts the given value after the given node.
        :param value: the value to insert
        :param node: value gets placed after this node
        :return: the new node
        """
        new_node = DoublyLinkedListNode(value)  # obtain an item a_ to hold value
        self._move_after(new_node, node)  # put it to the right place
        return new_node

    def _insert_before(self, value: Any, node: DoublyLinkedListNode) \
            -> DoublyLinkedListNode:
        """
        Inserts the given value before the given node.
        :param value: the value to insert
        :param node: value gets placed before this node
        :return: the new node
        """
        return self._insert_after(value, node.prev)

    def insert_at(self, i: int, value: int) -> None:
        """
        Inserts the given value at the i-th position
        :param i: the i-th position
        :param value: the inserted value
        :return: None
        """
        current = self.head.next
        index = 0
        while index < i and current is not self.head:
            if index == i:
                self._insert_before(value, current)
                return
            current = current.next

    def push_front(self, value: Any) -> None:
        """
        Pushes the given value to the head of the list
        :param value: the new head
        :return: None
        """
        self._insert_before(value, self.head)

    def push_back(self, value: Any) -> None:
        """
        Pushes the given value to the tail of the list
        :param value: the new tail
        :return: None
        """
        self._insert_after(value, self.head.prev)

    def concat(self, other_list) -> None:
        """
        Concatenates this list with other_list
        :type other_list: LinkedList
        :param other_list: the list to concatenate
        :return: None
        """
        if other_list.is_empty():
            return
        self._splice(other_list.head.next,
                     other_list.head.prev,
                     self.head.prev)

    def clear(self) -> None:
        """
        Clears the list in constant time.

        :return: None
        """
        trash = LinkedList()

        trash.concat(self)
        del trash

    def find(self, value: Any) -> DoublyLinkedListNode:
        current = self.first()

        # sentinel
        self.head.value = value

        while current.value != value:
            current = current.next

        if current != self.head:
            return current

    def size(self) -> int:
        """
        Calculates the size of the list in !! linear time !!
        :return: the size of the list
        """
        size = 0
        if self.is_empty():
            return size
        current = self.first()
        while current and current is not self.head:
            size += 1
            current = current.next
        return size

    def from_iterable(self, data: List[Any]):
        for item in data:
            self.push_back(item)

    def to_array(self) -> List[Any]:
        """
        Returns a copy of this list as a python list.
        :return: a copy of this list as a python list
        """
        arr = []
        for value in self:
            arr.append(value)
        return arr

    def unique_element_count(self):
        """
        Returns the number of unique elements
        :return: the number of unique elements
        """
        unique = set(self)
        return len(unique)
