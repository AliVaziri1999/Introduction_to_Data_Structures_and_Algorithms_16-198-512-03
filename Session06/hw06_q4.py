class BST:

    class Node:
        def __init__(self, key, value):
                self.key = key
                self.value = value
                self.left = None
                self.right = None


    class BST:
        def __init__(self):
                self.root = None

    def only_children(self):
        return self._only_children(self.root)

    def _only_children(self, x):

        if x is None:
            return 0

        one = 1 if ((x.left is None and x.right is not None) or
                    (x.left is not None and x.right is None)) else 0
        return one + self._only_children(x.left) + self._only_children(x.right)