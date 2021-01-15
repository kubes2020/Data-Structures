"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:  # The "is" operator compares the identity of two objects while "==" compares the value of two objects
            self.head = new_node
            self.tail = new_node
            return  # You could use "break" here instead, but it would still continue to line 20 so maybe don't. Return will end the function
        self.tail.next = new_node
        self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value)  # Created the new_node
        if self.head is None:  # Just in case there isn't already a head, meaning the list is empty
            self.head = new_node
            self.tail = new_node
            return
        # This way, the old head doesn't disappear and we can link it to the new one
        old_head = self.head
        self.head = new_node  # Assigning the new_node to the head
        self.head.next = old_head  # Reassigning the old head to the next of the new one

    def remove_head(self):
        if self.head is None:  # There's nothing to remove if the list is empty, which it is if head is empty
            return
        data = self.head.get_value()
        self.head = self.head.next
        return data

    def remove_tail(self):
        data = self.tail.get_value()
        cursor = self.head  # Can also be pointer. Start at the head
        # Using cursor.next.next so that when the next item of our next item is none, we know that our item is the item before the tail
        while cursor.next.next is not None:  # We don't know how long the list is, hence a while loop
            cursor = cursor.next  # Move the cursor to the next one
        self.tail = cursor  # Set linked list's tail to the cursor
        self.tail.next = None  # Get rid of the connection/arrow to the old tail
        return data


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1  # self.size = self.size + 1 (same thing)
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return
        self.size -= 1  # self.size = self.size - 1 (same thing)
        return self.storage.remove_head()


class Stack:
    def __init__(self):
        self.size = 0  # Keep track of the length. You could do this in the linked list class
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1  # Keep track of the length
        # We've chosen to add/remove from the start
        return self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:
            return
        self.size -= 1  # Keep track of the length
        return self.storage.remove_head()


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # with recursion
        # max_value = self.value
        # if max_value is not None:
        #     if self.right is None:
        #         return max_value
        #     else:
        #         return self.right.get_max()
        # else:
        #     return None

        # with while loop
        current_node = self
        if current_node == None:
            return None
        while current_node.right:
            current_node = current_node.right
        max_value = current_node.value
        return max_value

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        if not self:
            return
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self is None:
            return
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        q = Queue()
        q.enqueue(self)
        while q.size != 0:
            current = q.dequeue()
            print(current.value)
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        s = Stack()
        s.push(self)
        while s.size != 0:
            current = s.pop()
            print(current.value)
            if current.left:
                s.push(current.left)
            if current.right:
                s.push(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT  #print before we check left and right
    def pre_order_dft(self):
        if self:
            print(self.value)
            if self.left:
                self.left.pre_order_dft()
            if self.right:
                self.right.pre_order_dft()

    # Print Post-order recursive DFT #check left and right then print
    def post_order_dft(self):
        if self:
            if self.left:
                self.left.post_order_dft()
            if self.right:
                self.riht.post_order_dft()
            print(self.value)


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()
