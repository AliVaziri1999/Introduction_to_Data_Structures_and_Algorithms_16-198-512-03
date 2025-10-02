# 1) size(): recursive count that does NOT use self._size
def size(self):
    """
    Return the number of nodes by walking the links recursively.
    Rules per assignment: do NOT use self._size.
    """
    def _count(node):
        # Base case: no node -> contributes 0 to the count
        if node is None:
            return 0
        # Recursive case: 1 (this node) + size of the rest
        return 1 + _count(node._next)

    return _count(self._head)


# 2) reverse(): in-place reversal of the links (O(n) time, O(1) extra space)
def reverse(self):
    """
    Reverse the list by flipping the 'next' pointers.
    We do NOT allocate any new nodes (only relink).
    Time: O(n) — we visit each node once
    Space: O(1) — just a few local pointers
    """
    prev = None
    curr = self._head

    # After reversal, the old head becomes the new tail
    self._tail = self._head

    # Standard in-place reverse of a singly linked list:
    #   curr -> next ; curr.next = prev ; advance both
    while curr is not None:
        nxt = curr._next     # save next node before we overwrite the link
        curr._next = prev    # flip the arrow
        prev = curr          # step prev forward
        curr = nxt           # step curr forward

    # prev now points to the old tail, which is the new head
    self._head = prev


# 3) removeDuplicates(): list is in ascending order; delete adjacent dupes in O(n)
def removeDuplicates(self):
    """
    Remove duplicates from a sorted (ascending) linked list.
    We do NOT create any new lists or auxiliary structures.
    Time: O(n) — single pass
    Space: O(1) — in-place
    """
    curr = self._head

    # Walk the list, comparing each node with its successor.
    while curr is not None and curr._next is not None:
        if curr._element == curr._next._element:
            # Duplicate found: unlink the next node
            dup = curr._next
            curr._next = dup._next
            self._size -= 1           # keep the stored size consistent

            # If we removed the last node, update tail
            if curr._next is None:
                self._tail = curr
        else:
            # No duplicate at this boundary; move forward
            curr = curr._next
