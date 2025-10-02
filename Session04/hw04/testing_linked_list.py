from linked_list import LinkedList
ll = LinkedList()
ll.add_to_front(3); ll.add_to_front(2); ll.add_to_front(2); ll.add_to_front(1)
print(ll)                  # 1 -> 2 -> 2 -> 3
print(len(ll))             # uses stored _size
print(ll.size())           # your recursive counter
ll.removeDuplicates()      # becomes 1 -> 2 -> 3
print(ll)
ll.reverse()               # becomes 3 -> 2 -> 1
print(ll)
