"""
Author: Ali Vaziri
Homework 8
Class: DSA 16-198-512-03
Fall 2025
"""
"""
For this assignment, you may add additional variables (e.g., integers) in the constructor 
to support your data structure's functionality, but you may not introduce any 
built-in data structures (such as lists, dictionaries, sets, etc.). 
Please keep your implementation within these guidelines.
"""

from queue import PriorityQueue

# Q1
class StackUsingPriorityQueue:
    def __init__(self):
        self.priority_queue = PriorityQueue()
        self._t = 0

    def push(self, item):
        self._t += 1
        self.priority_queue.put((-self._t, item))

    def pop(self):
        if self.priority_queue.qsize() == 0:
            raise IndexError("pop from empty stack")
        return self.priority_queue.get()[1]

    def is_empty(self):
        return self.priority_queue.qsize() == 0


# Q1 - tests :
s = StackUsingPriorityQueue()
for x in [1, 2, 3, 4, 5]:
    s.push(x)
_stack_popped = []
while not s.is_empty():
    _stack_popped.append(s.pop())
print("Q1: Stack LIFO  ->", _stack_popped, "Result: [5, 4, 3, 2, 1]")
'''
Output:

Q1: Stack LIFO  -> [5, 4, 3, 2, 1] Result: [5, 4, 3, 2, 1]
'''



# Q2
class QueueUsingPriorityQueue:
    def __init__(self):
        self.priority_queue = PriorityQueue()
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


# Q2 - tests:
q = QueueUsingPriorityQueue()
for x in [10, 20, 30, 40, 50]:
    q.enqueue(x)
_queue_dequeued = []
while not q.is_empty():
    _queue_dequeued.append(q.dequeue())
print("Q2: Queue FIFO  ->", _queue_dequeued, "Result: [10, 20, 30, 40, 50]")
'''
Output:

Q2: Queue FIFO  -> [10, 20, 30, 40, 50] Result: [10, 20, 30, 40, 50]
'''


# Q3
def findKthElement(lst, k):

    if not 1 <= k <= len(lst):
        raise ValueError("k must be between 1 and length of lst")

    min_heap = PriorityQueue(maxsize=k)

    for x in lst:
        if min_heap.qsize() < k:
            min_heap.put(x)
        else:
            smallest = min_heap.get()
            if x > smallest:
                min_heap.put(x)
            else:
                min_heap.put(smallest)

    return min_heap.get()


# Q3 - tests:
_lst1 = [3, 2, 1, 5, 9, 4]; _k1 = 2
_lst2 = [3, 2, 3, 0, 2, 4, 5, 7, 6]; _k2 = 4
print("Q3: Ex 1 ->", findKthElement(_lst1, _k1), "Result: 5")
print("Q3: Ex 2 ->", findKthElement(_lst2, _k2), "Result: 4")
'''
Output:

Q3: Ex 1 -> 5 Result: 5
Q3: Ex 2 -> 4 Result: 4
'''