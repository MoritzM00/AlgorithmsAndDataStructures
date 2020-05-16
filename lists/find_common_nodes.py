from lists.node import Node


def has_common_node(node1: Node, node2: Node):
    """
    Checks if two lists have a common node.

    Two lists have a common node if one node points to another node in the other list.
    :param node1: the head of the first list
    :param node2: the head of the second list
    :return: true if they have a common node
    """
    while node1 is not None or node2 is not None:
        if node1 is not None:
            node1 = node1.next
        if node2 is not None:
            node2 = node2.next
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


def find_common_helper(node1, node2):
    while node1 is not None and node2 is not None:
        if node1 == node2:
            # first common node
            return node1
        else:
            node1 = node1.next
            node2 = node2.next
    # no common node found
    return None


def find_first_common_node(node1, node2):
    """
    Returns the first common node of two lists.
    :param node1: the head of the first list
    :param node2: the head of the second list
    :return: the first common node of two lists
    """
    size1 = get_size(node1)
    size2 = get_size(node2)
    diff = abs(size1 - size2)

    if size1 > size2:
        # move forward in the bigger list, so that the elements can be compared side by side
        return find_common_helper(get_nth_node(node1, diff - 1), node2)
    else:
        return find_common_helper(get_nth_node(node2, diff - 1), node1)
