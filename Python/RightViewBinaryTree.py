"""
Given a binary tree find the left view of the binary tree

          6
       5     8
     3   4 7   9
     Left View: 6 8 9

          11
        2   13
           12
     Left View: 11, 13, 12
"""


class BinaryTree:
    def __init__(self, val):
        self.left = None
        self.value = val
        self.right = None

    def insert_node(self, val):
        if self.value:
            if val < self.value:
                if not self.left:
                    self.left = BinaryTree(val)
                else:
                    self.left.insert_node(val)
            else:
                if not self.right:
                    self.right = BinaryTree(val)
                else:
                    self.right.insert_node(val)
        else:
            self.value = val

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value, end=" ")
        if self.right:
            self.right.print_tree()


def right_view_util(root, level, max_level):
    if not root:
        return
    if max_level[0] < level:
        print(root.value, end=" ")
        max_level[0] = level
    count = level + 1
    right_view_util(root.right, count, max_level)
    right_view_util(root.left, count, max_level)


def right_view(root_node):
    max_level = [0]
    right_view_util(root_node, 1, max_level)


if __name__ == "__main__":
    root = BinaryTree(11)
    root.insert_node(2)
    root.insert_node(13)
    root.insert_node(12)
    # root.print_tree()
    right_view(root)
