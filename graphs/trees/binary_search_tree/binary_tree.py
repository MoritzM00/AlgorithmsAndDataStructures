from queues.queue import Queue

from trees.node import Node


class BTree:
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    @staticmethod
    def compare(node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    def insert_with_loop(self, value):
        new_node = Node(value)
        node = self.get_root()
        if not node:
            self.root = new_node
            return
        while True:
            comp = self.compare(node, new_node)
            if comp == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break
            elif comp == 1:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break
            else:
                node.set_value(value)
                break

    """
    define insert here (can use recursion)
    try one or both ways
    """

    def insert_with_recursion(self, value):
        root = self.get_root()
        # base case
        if root is None:
            self.set_root(value)
        else:
            self.insert_recursively(root, Node(value))

    def insert_recursively(self, node, new_node):
        comp = self.compare(node, new_node)
        if comp == 0:
            # equal
            node.set_value(new_node.get_value())
        elif comp == -1:
            # traverse left
            if node.has_left_child():
                self.insert_recursively(node.get_left_child(), new_node)
            else:
                node.set_left_child(new_node)
        else:
            # traverse right
            if node.has_right_child():
                self.insert_recursively(node.get_right_child(), new_node)
            else:
                node.set_right_child(new_node)

    """
    implement search
    """
    def search(self, value):
        root = self.get_root()
        if not root:
            return False
        else:
            return self.search_recursively(root, value)

    def search_recursively(self, node, value):
        if node:
            node_val = node.get_value()
            if node_val == value:
                return True
            elif node_val > value:
                return self.search_recursively(node.get_left_child(), value)
            else:
                return self.search_recursively(node.get_right_child(), value)
        else:
            return False

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while len(q) > 0:
            node, level = q.deq()
            if node is None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s
