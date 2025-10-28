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
    
    def push(self, item):
        # Complete this method
    
    def pop(self):
        # Complete this method
    
    def is_empty(self):
        # Complete this method
        



# Q2
class QueueUsingPriorityQueue:
    def __init__(self):
        self.priority_queue = PriorityQueue()
    
    def enqueue(self, item):
        # Complete this method
    
    def dequeue(self):
        # Complete this method
    
    def is_empty(self):
        # Complete this method
        
        


#Q3
def findKthElement(lst, k):
    min_heap = PriorityQueue(maxsize=k)
    # Complete this function. You are not allowed to add any other variables in this function.


