'''
class BST:
    # ... keep your existing code ...

    # Delete using the node on the LEFT side (predecessor)
    def delete_left(self, key):
        self.root = self._delete_left(self.root, key)

    def _delete_left(self, x, key):
        if x is None:
            return None
        if key < x.key:
            x.left = self._delete_left(x.left, key)
        elif key > x.key:
            x.right = self._delete_left(x.right, key)
        else:
            # case: 0 or 1 child
            if x.left is None:
                return x.right
            if x.right is None:
                return x.left
            # case: 2 children — replace with predecessor (max of left)
            t = x
            x = self._max(t.left)
            x.left = self._deleteMax(t.left)
            x.right = t.right
        x.N = self._size(x.left) + self._size(x.right) + 1
        return x

    # helpers symmetric to _min / _deleteMin already in bst.py
    def _max(self, x):
        while x.right is not None:
            x = x.right
        return x

    def delete_max(self):
        self.root = self._deleteMax(self.root)

    def _deleteMax(self, x):
        if x.right is None:
            return x.left
        x.right = self._deleteMax(x.right)
        x.N = self._size(x.left) + self._size(x.right) + 1
        return x
'''




def delete_left(self, key):
    self.root = self._delete_left(self.root, key)

def _delete_left(self, x, key):
    if x is None:
        return None
    if key < x.key:
        x.left = self._delete_left(x.left, key)
    elif key > x.key:
        x.right = self._delete_left(x.right, key)
    else:

        if x.left is None: # 0 or 1 child
            return x.right
        if x.right is None:
            return x.left

        t = x # 2 children replace with predecessor from the left side
        x = self._max(t.left) # predecessor
        x.left  = self._deleteMax(t.left)
        x.right = t.right

    x.N = self._size(x.left) + self._size(x.right) + 1
    return x

def _max(self, x):
    while x.right is not None:
        x = x.right
    return x

def delete_max(self):
    self.root = self._deleteMax(self.root)

def _deleteMax(self, x):
    if x.right is None:
        return x.left
    x.right = self._deleteMax(x.right)
    x.N = self._size(x.left) + self._size(x.right) + 1
    return x