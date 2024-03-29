__author__ = 'hnng'
print "test"
import itertools


class Tree(object):
    def __init__(self, val, distance=0, left=None, right=None, parent=None):
        self.parent = parent
        self.distance = distance
        self.left = left
        self.right = right
        self.val = val

    def show(self, ord=''):
        print ord, self.val
        if self.left:
            self.left.show(ord=ord + '\t')
        if self.right:
            self.right.show(ord=ord + '\t')


    def insert_node(self, left_val, right_val):
        self.left = Tree(left_val, distance=self.distance + 1, parent=self)
        self.right = Tree(right_val, distance=self.distance + 1, parent=self)

    def insert_tree(self, left_tree, right_tree):
        self.left = left_tree
        if self.left:
            self.left.parent = self
            self.left.distance = self.distance + 1
        self.right = right_tree
        if self.right:
            self.right.parent = self
            self.right.distance = self.distance + 1

    def find_node(self, node_val):
        for node in self.traverse_tree():
            if node.val == node_val:
                return node
        return

    def traverse_tree(self):
        yield self
        if self.left:
            for tree in self.left.traverse_tree():
                yield tree
        if self.right:
            for tree in self.right.traverse_tree():
                yield tree

    def is_leaf(self):
        return not self.left and not self.right

    def iter_leaf(self):
        for tree in self.traverse_tree():
            if tree.is_leaf():
                yield tree

    def is_balanced(self):
        print "balanced"
        for first, second in itertools.combinations(self.iter_leaf(), 2):
            print first.val, first.distance, second.val, second.distance
            if abs(first.distance - second.distance) > 1:
                return False
        return True

    def find_parent_node(self, node1, node2):
        if not node1 or not node2:
            return None
        elif node1.parent == node2.parent:
            return node1.parent
        else:
            return self.find_parent_node(node1.parent, node2.parent)

    def find_parent(self, node_val_1, node_val_2):
        node_1 = self.find_node(node_val_1)
        node_2 = self.find_node(node_val_2)
        return self.find_parent_node(node_1, node_2)

    def is_identical(self, tree):
        if not tree:
            return False
        if not self.val == tree.val:
            return False
        identical_left = False
        if self.left:
            identical_left = self.left.is_identical(tree.left)
        else:
            identical_left = not tree.left
        identical_right = False
        if self.right:
            identical_right = self.right.is_identical(tree.right)
        else:
            identical_right = not tree.right
        return identical_left and identical_right


    def sub_tree(self, tree):
        node = self.find_node(tree.val)
        if not node:
            return False
        else:
            return node.is_identical(tree)

def BinaryTree(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = None
        self.left = None
        self.right = None


def test_tree():
    t = Tree(0)
    t.insert_node(1, 2)
    t.right.insert_node(3, 4)
    t.right.right.insert_node(5, 6)
    t.left.insert_node(7, 8)
    t.show()
    for node in t.iter_leaf():
        print node.val, node.distance
    print t.is_balanced()


def is_linked(graph, a, b):
    if a not in graph:
        return False
    for node in graph[a]:
        if node == b:
            return True
        if is_linked(graph, node, b):
            return True
    return False

def test_graph():
    graph = {
    1: [3, 4, 5],
    3: [7, 8],
    4: [3, 5, 2]
    }
    print is_linked(graph, 7, 8)
    print is_linked(graph, 1, 5)


def create_tree(sorted_list):
    if not sorted_list:
        return None
    if len(sorted_list) == 1:
        return Tree(val=sorted_list[0])

    index = len(sorted_list) / 2
    root = sorted_list[index]

    left = create_tree(sorted_list[:index]) if index > 0 else None
    right = create_tree(sorted_list[index + 1:]) if index < len(sorted_list) - 1 else None
    tree = Tree(root)
    tree.insert_tree(left, right)
    return tree

def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n

if __name__ == '__main__':
    print factorial(10)
