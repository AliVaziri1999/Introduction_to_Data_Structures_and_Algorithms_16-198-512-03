"""
xxx
"""

from queue import PriorityQueue

# Q1
class StackUsingPriorityQueue:
    def __init__(self):
        self.priority_queue = PriorityQueue()
        # Newest items should come out first from a MIN-PQ → store (-time, item)
        self._t = 0

    def push(self, item):
        self._t += 1
        self.priority_queue.put((-self._t, item))

    def pop(self):
        if self.priority_queue.qsize() == 0:
            raise IndexError("pop from empty stack")
        # get() returns (priority, payload)
        return self.priority_queue.get()[1]

    def is_empty(self):
        return self.priority_queue.qsize() == 0


# Q2
class QueueUsingPriorityQueue:
    def __init__(self):
        self.priority_queue = PriorityQueue()
        # Earlier enqueued items should come out first → store (+time, item)
        self._t = 0

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
    """
    Return the k-th largest element in lst without sorting.
    Keep a size-k MIN-heap of the largest values seen so far.
    After the scan, the smallest in that heap is the k-th largest overall.
    """
    if not 1 <= k <= len(lst):
        raise ValueError("k must be between 1 and len(lst)")

    min_heap = PriorityQueue(maxsize=k)

    for x in lst:
        if min_heap.qsize() < k:
            # Still filling the heap
            min_heap.put(x)
        else:
            # Compare with current smallest (the k-th so far)
            smallest = min_heap.get()
            if x > smallest:
                # x joins the top-k
                min_heap.put(x)
            else:
                # keep the previous k-th
                min_heap.put(smallest)

    # The k-th largest is the smallest element remaining in the heap
    return min_heap.get()
