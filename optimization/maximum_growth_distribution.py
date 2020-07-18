from lists.doubly_linked_list import LinkedList


def maximize_growth(T) -> int:
    """
    Let {1,2,3} be three different sorts of food.
    Optimize the distribution of the different sorts of food to two animals which grow at different
    rates. If the animal gets 3 three different sorts, it grows +3, if it gets two different sorts it grows +2
    and if it gets only one different sort, it grows +1.

    Maximizes the "growth" for both animals for an Array of {1,2,3} of size n.
    :param T: An Array containing of {1,2,3} and size n.
    :return: Max growth
    """
    g = 0
    m1 = LinkedList()
    m2 = LinkedList()

    for i in range(len(T)):
        if T[i] in m1:
            m2.push_back(T[i])
        elif T[i] in m2:
            m1.push_back(T[i])
            if m1.unique_element_count() < m2.unique_element_count():
                m1.pop_back()
                m2.push_back(T[i])
        else:
            m1.push_back(T[i])

        if len(m1) == 3:
            g += m1.unique_element_count()
            m1.clear()
        if len(m2) == 3:
            g += m2.unique_element_count()
            m2.clear()
    return g
