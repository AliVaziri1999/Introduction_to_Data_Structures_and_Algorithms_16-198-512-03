class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def next(self, target):
        return self._next(self.root, target)

    def _next(self, x, target):
        if x is None:
            return None

        if x.key > target:
            left_ans = self._next(x.left, target) # the left subtree
            return left_ans if left_ans is not None else x.key

        else:
            return self._next(x.right, target) # if x.key <= target so, target in the right subtree
