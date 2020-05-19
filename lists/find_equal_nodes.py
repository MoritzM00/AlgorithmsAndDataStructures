from lists.node import Node


def has_equal_node(node1: Node, node2: Node):
    """
    Checks if two lists have an equal node.

    Two lists have an equal node if one node points to another node in the other list.
    :param node1: the head of the first list
    :param node2: the head of the second list
    :return: true if they have an equal node
    """
    # iterate to the end of both lists
    while node1 is not None:
        node1 = node1.next
    while node2 is not None:
        node2 = node2.next
    # if they have an equal node, then all nodes behind that one must be equal
    # too, so it is enough to check for the last node
    return node1 == node2


def get_size(head: Node):
    """
    Returns the size of a list.
    :param head: the head of the list
    :return: the size of the list
    """
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


def get_nth_node(head: Node, n: int):
    """
    Returns the nth node of the list
    :param head: the head of the list
    :param n: the nth node
    :return: the nth node
    """
    current = 0
    while current < n:
        if head is None:
            return None
        else:
            head = head.next
    return head


def find_equal_helper(node1, node2):
    while node1 is not None and node2 is not None:
        if node1 == node2:
            # first equal node
            return node1
        else:
            node1 = node1.next
            node2 = node2.next
    # no equal node found
    return None


def find_first_equal_node(node1, node2):
    """
    Returns the first equal node of two lists.
    :param node1: the head of the first list
    :param node2: the head of the second list
    :return: the first equal node of two lists
    """
    size1 = get_size(node1)
    size2 = get_size(node2)
    diff = abs(size1 - size2)

    if size1 > size2:
        # move forward in the bigger list, so that the elements can be compared side by side
        return find_equal_helper(get_nth_node(node1, diff - 1), node2)
    else:
        return find_equal_helper(get_nth_node(node2, diff - 1), node1)
