'''
        Stack
'''
# stack = [1, 2, 3]
# print(stack)
#
# stack.append(4)
# print(stack)
#
# stack.append(5)
# print(stack)
#
# stack.append(6)
# print(stack)
#
# stack.append(7)
# print(stack)
#
# stack.pop()
# print(stack)

'''
        Queue
'''
from queue import Queue

q = Queue()
# print(q.qsize())
# Peek at contents (without losing them)
items = list(q.queue)   # internal deque object
print(items)             # [5, 10, 15]

q.put(5)   # enqueue
# Peek at contents (without losing them)
items = list(q.queue)   # internal deque object
print(items)             # [5, 10, 15]

q.put(2)   # enqueue
# Peek at contents (without losing them)
items = list(q.queue)   # internal deque object
print(items)             # [5, 10, 15]

a = q.get()    # dequeue
# Peek at contents (without losing them)
items = list(q.queue)   # internal deque object
print(items)             # [5, 10, 15]

b = a * 2
print(b)

'''

'''