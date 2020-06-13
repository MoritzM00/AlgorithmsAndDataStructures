from lists.doubly_linked_list import LinkedList
from math import inf


def find_min(lists) -> (bool, float):
    """
    Returns the minimum of an given array of Linked Lists.
    :param lists: an array-like data structure containing sorted lists
    :return: a tuple of a boolean and an int, indicating whether a min has been found
             and the minimum element itself
    """
    min = inf
    current_lst_index = -1
    for j, lst in enumerate(lists):
        if not lst.is_empty() and lst.first() < min:
            min = lst.head()
            current_lst_index = j
    b = current_lst_index != -1
    if b:
        lists[current_lst_index].pop_front()
    return b, min


def k_way_merge(lists) -> LinkedList:
    """
    Merges k sorted Linked Lists into one big Linked List
    :param lists: an array-like data structure containing sorted Linked Lists
    :return: a big sorted Linked List
    """
    result = LinkedList()
    found, min = find_min(lists)
    while found:
        result.push_back(min)
        found, min = find_min(lists)
    return result
