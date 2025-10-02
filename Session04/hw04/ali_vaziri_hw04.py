# HW04
# Class: Introduction to Data Structures and Algorithms - 16:198:512:03
# Professor: Dr. Kreutzer
# Fall 2025
# Author: Ali Vaziri


# 1- return the number of nodes by going the links recursively
def size(self):

    def _count(node):
        if node is None: # base case --> no node
            return 0

        return 1 + _count(node._next) # recursive case --> 1 (this node) + the rest size

    return _count(self._head)


# 2- reverse the list by flipping the "next" pointers
def reverse(self):

    prev = None
    curr = self._head
    self._tail = self._head # after reversal the old head becomes the new tail

    while curr is not None:
        next = curr._next # save next node before we overwrite the link
        curr._next = prev # flip the arrow
        prev = curr # step prev forward
        curr = next # step curr forward
        # prev now points to the old tail, which is the new head

    self._head = prev


# 3- remove duplicates from linked list
def removeDuplicates(self):

    curr = self._head

    while curr is not None and curr._next is not None: # walk in the list and comparing each node
        if curr._element == curr._next._element:# duplicate found, unlink the next node
            dup = curr._next
            curr._next = dup._next
            self._size -= 1 # stored size consistent

            if curr._next is None: # update tail because removed the last node
                self._tail = curr
        else:
            curr = curr._next # move forward no duplicate