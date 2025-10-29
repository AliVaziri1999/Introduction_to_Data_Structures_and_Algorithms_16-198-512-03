"""
Author: Ali Vaziri
Homework 8
Class: DSA 16-198-512-03
Fall 2025
"""

from queue import PriorityQueue, Empty

# Q1
class StackUsingPriorityQueue:
    def __init__(self):
        self.priority_queue = PriorityQueue()
        self._t = 0 # store counter item so the newest has the smallest key

    def push(self, item):
        self._t += 1
        self.priority_queue.put((-self._t, item))

    def pop(self):
        if self.priority_queue.qsize() == 0:
            raise IndexError("pop from empty stack")

        return self.priority_queue.get()[1]

    def is_empty(self):
        return self.priority_queue.qsize() == 0


# Q2
class QueueUsingPriorityQueue:
    def __init__(self):
        self.priority_queue = PriorityQueue()
        self._t = 0 # timestamp grows with each enqueue

    def enqueue(self, item):
        self._t += 1
        self.priority_queue.put((self._t, item))

    def dequeue(self):
        if self.priority_queue.qsize() == 0:
            raise IndexError("dequeue from empty queue")
        return self.priority_queue.get()[1]

    def is_empty(self):
        return self.priority_queue.qsize() == 0


# Q3
def findKthElement(lst, k):

    if not 1 <= k <= len(lst):
        raise ValueError("k must be between 1 and len(lst)")

    min_heap = PriorityQueue(maxsize=k)

    for x in lst:
        if min_heap.qsize() < k: # if we still have room just put x
            min_heap.put(x)
        else:
            smallest = min_heap.get() # remove current smallest and compare to x
            if x > smallest:
                min_heap.put(x) # x in the top-k so keep it
            else:
                min_heap.put(smallest) # x doesn't the current k-th so restore smallest

    # now the heap holds exactly k elements meaning the largest.
    while min_heap.qsize() > 1: # Pop until one remains that last one is the k-th largest.
        min_heap.get()
    return min_heap.get()




