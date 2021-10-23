from trees.node import Node


class Tree:
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

    # depth first search algorithms


# 1) pre order:
def pre_order(tree):
    """
    Traverses a tree depth first by pre-order
    :param tree:
    :return:
    """
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            # add to visit order
            visit_order.append(node.get_value())

            # visit left
            traverse(node.get_left_child())

            # visit right
            traverse(node.get_right_child())

    traverse(root)

    return visit_order


# 2) in order
def in_order(tree):
    visit_order = []
    root = tree.get_root()

    def traverse(node):
        if node:
            traverse(node.get_left_child())

            visit_order.append(node.get_value())

            traverse(node.get_right_child())

    traverse(root)

    return visit_order


# 3) post order
def post_order(tree):
    visit_order = []
    root = tree.get_root()

    def traverse(node):
        if node:
            traverse(node.get_left_child())

            traverse(node.get_right_child())

            visit_order.append(node.get_value())

    traverse(root)

    return visit_order
