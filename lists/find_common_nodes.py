from lists.node import Node


def has_common_node(n1: Node, n2: Node):
    while n1 is not None or n2 is not None:
        if n1 is not None:
            n1 = n1.next
        if n2 is not None:
            n2 = n2.next
    return n1 == n2


def get_size(node: Node):
    count = 0
    while node is not None:
        count += 1
        node = node.next
    return count


def get_nth_node(head: Node, n: int):
    current = 0
    while current < n:
        if head is None:
            return None
        else:
            head = head.next
    return head


def find_common_helper(n1, n2):
    while n1 is not None and n2 is not None:
        if n1 == n2:
            return n1
        else:
            n1 = n1.next
            n2 = n2.next
    return None


def find_first_common_node(n1, n2):
    size1 = get_size(n1)
    size2 = get_size(n2)
    diff = abs(size1 - size2)

    if size1 > size2:
        # move forward in the bigger list, so that the elements can be compared side by side
        return find_common_helper(get_nth_node(n1, diff - 1), n2)
    else:
        return find_common_helper(get_nth_node(n2, diff - 1), n1)
