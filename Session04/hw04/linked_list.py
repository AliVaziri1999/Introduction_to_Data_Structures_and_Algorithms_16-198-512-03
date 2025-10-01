class LinkedList:

  #-------------------------- nested _Node class --------------------------
  class _Node:
    __slots__ = '_element', '_next'         # streamline memory usage

    def __init__(self, element, next):
      self._element = element
      self._next = next

  #------------------------------- list methods -------------------------------
  def __init__(self):
    self._head = None
    self._tail = None
    self._size = 0                          

  def __len__(self):
    return self._size

  def is_empty(self):
    return self._size == 0

  def front(self):
    if self.is_empty():
      raise ValueError('list is empty')
    return self._head._element              # front aligned with head of list

  def remove_front(self):
    if self.is_empty():
      raise ValueError('list is empty')
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    if self.is_empty():                     # special case as list is empty
      self._tail = None                     # removed head had been the tail
    return answer
  
  def add_to_front(self, e):
      self._head = self._Node(e, self._head)   
      if self.is_empty():
            self._tail = self._head
      self._size += 1
  
  def add_to_rear(self, e):
      newest = self._Node(e, None)            # node will be new tail node
      if self.is_empty():
          self._head = newest                   # special case: previously empty
      else:
          self._tail._next = newest
      self._tail = newest                     # update reference to tail node
      self._size += 1

  def __repr__(self):
      elements = []
      cursor = self._head 
      while cursor is not None:
          elements.append(str(cursor._element))
          cursor = cursor._next
      
      return " -> ".join(elements)

  def find(self, e):
      cursor = self._head 
      while cursor is not None:
          if cursor._element == e:
              return cursor
          cursor = cursor._next

  def findPredecessor(self, e):
      predecessor = None
      cursor = self._head 
      while cursor is not None:
          if cursor._element == e:
              return predecessor, cursor
          predecessor = cursor
          cursor = cursor._next      
 
  def insert(self, insertAt, e):
      predecessor, cursor = self.findPredecessor(insertAt)
      if cursor is None:
          raise ValueError('Not in list')
          
      if predecessor is None:
          self.add_to_front(e)
      else:
          predecessor._next = self._Node(e, cursor)
          
  def delete(self, e):
      predecessor, cursor = self.findPredecessor(e)
      if cursor is None:
          raise ValueError('Not in list')
          
      if predecessor is None:
          self.remove_front()
      else:
          predecessor._next = cursor._next
          if self._tail == cursor:
              self._tail = predecessor
  
if __name__ == '__main__':
    ll = LinkedList()
    for i in range(5):
        ll.add_to_front(i)
        
    print(ll)
        
  