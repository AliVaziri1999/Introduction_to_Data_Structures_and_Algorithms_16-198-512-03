# file: test_hw04.py   (put this next to linked_list.py)

from linked_list import LinkedList

# --- your three functions (standalone) ---
def size(self):
    def _count(node):
        if node is None:
            return 0
        return 1 + _count(node._next)
    return _count(self._head)

def reverse(self):
    prev = None
    curr = self._head
    self._tail = self._head  # old head becomes new tail
    while curr is not None:
        nxt = curr._next
        curr._next = prev
        prev = curr
        curr = nxt
    self._head = prev

def removeDuplicates(self):
    curr = self._head
    while curr is not None and curr._next is not None:
        if curr._element == curr._next._element:
            curr._next = curr._next._next
            self._size -= 1
            if curr._next is None:
                self._tail = curr
        else:
            curr = curr._next

# --- bind them onto the imported class (no edit to linked_list.py) ---
LinkedList.size = size
LinkedList.reverse = reverse
LinkedList.removeDuplicates = removeDuplicates

# --- now test ---
ll = LinkedList()
for x in [1, 1, 2, 3, 3]:
    ll.add_to_rear(x)

print("start:   ", ll, "| size()", ll.size())     # expect: 1 -> 1 -> 2 -> 3 -> 3 | 5
ll.removeDuplicates()
print("dedup:   ", ll, "| size()", ll.size())     # expect: 1 -> 2 -> 3 | 3
ll.reverse()
print("reverse: ", ll, "| size()", ll.size())     # expect: 3 -> 2 -> 1 | 3
