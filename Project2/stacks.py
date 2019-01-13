
class StackArray:
    """Implements an efficient last-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity= capacity
        self.items = [None]*capacity
        self.num_items = 0 

    def is_empty(self):
        """Returns true if the stack self is empty and false otherwise"""
        return self.num_items == 0

    def is_full(self):
        """Returns true if the stack self is full and false otherwise"""
        return self.num_items == self.capacity

    def push(self, item):
        """Returns puts item on the top of the Stack"""
        self.items[self.num_items]=item
        self.num_items += 1

    def pop(self):
        """Returns item on the top of the stack and removes it"""
        self.num_items -= 1
        return self.items[self.num_items]

    def peek(self):
        """Returns item on the top of the stack but does not remove it"""
        return self.items[self.num_items-1]

    def size(self):
       """Returns the number of items in the stack"""
       return self.num_items

