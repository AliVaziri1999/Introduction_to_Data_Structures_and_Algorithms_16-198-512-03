# HW04
# Class: Introduction to Data Structures and Algorithms - 16:198:512:03
# Professor: Dr. Kreutzer
# Fall 2025
# Author: Ali Vaziri

# 1. return the number of nodes by recursion
def size(self):
    def _count(node):
        if node is None:
            return 0
        return 1 + _count(node._next)

    return _count(self._head)


# 2. reverse the list in place
def reverse(self):

    prev = None
    curr = self._head

    self._tail = self._head # old head will become the new tail

    while curr is not None:
        nxt = curr._next # remember next node
        curr._next = prev # flip link
        prev = curr
        curr = nxt

    self._head = prev # prev is the old tail (new head)


# 3. remove duplicates from a sorted list
def removeDuplicates(self):

    curr = self._head
    while curr is not None and curr._next is not None:
        if curr._element == curr._next._element: # skip the duplicate node

            curr._next = curr._next._next
            self._size -= 1
            if curr._next is None: # we removed the last node
                self._tail = curr
        else:
            curr = curr._next



# Test case:

'''
from linked_list import LinkedList

ll = LinkedList()
for x in [1, 1, 2, 3, 3]:
    ll.add_to_rear(x)

print("start:   ", ll, "| size()", ll.size())    

ll.removeDuplicates()
print("dedup:   ", ll, "| size()", ll.size())    

ll.reverse()
print("reverse: ", ll, "| size()", ll.size())     

'''

# The output of Test:

'''
start:    1 -> 1 -> 2 -> 3 -> 3 | size() 5
dedup:    1 -> 2 -> 3 | size() 3
reverse:  3 -> 2 -> 1 | size() 3
'''