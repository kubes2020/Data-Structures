from singly_linked_list import LinkedList
import sys
import os
sys.path.append(os.path.join(os.path.dirname(
    sys.path[0]), 'singly_linked_list'))

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList() # this is the stack

#     def __len__(self):
#         return self.size

#     def push(self, value): # increment size by one
#         self.size += 1
#         return self.storage.add_to_head(value)
#     def pop(self):
#         if self.size == 0:
#             return
#         self.size -= 1
#         return self.storage.remove_head()


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []  # this is the stack

    def __len__(self):
        return len(self.storage)

    def push(self, value):  # increment size by one
        self.size += 1
        return self.storage.insert(0, value)

        # or add to tail
        # return self.storage.append(value)

    def pop(self):
        if len(self.storage) == 0:
            return
        self.size -= 1
        remove_item = self.storage[0]
        del self.storage[0]
        return remove_item

        # remove_item = self.storage[-1]
        # del self.storage[-1]
        # return remove_item
