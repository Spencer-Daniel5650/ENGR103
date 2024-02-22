# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/21/2024
# Description:The code implements a recursive LinkedList class with methods
# for manipulation and conversion to a Python list

class Node:
    """A Node class for LinkedList that stores data and a reference to the next node."""
    def __init__(self, data):
        """Initialize a new node with the given data and no next node."""
        self.data = data
        self.next = None


class LinkedList:
    """LinkedList class with recursive methods for linked list manipulation."""
    def __init__(self):
        """Initialize a LinkedList with a private head node."""
        self.__head = None

    def get_head(self):
        """Return the head of the list."""
        return self.__head

    def add(self, value, current=None):
        """Add a value to the end of the list recursively."""
        if current is None:
            current = self.__head
        if current is None:
            self.__head = Node(value)
        elif current.next is None:
            current.next = Node(value)
        else:
            self.add(value, current.next)

    def remove(self, value, current=None, previous=None):
        """Remove the first occurrence of value in the list recursively."""
        if current is None:
            current = self.__head
        if current:
            if current.data == value:
                if previous is None:
                    self.__head = current.next
                else:
                    previous.next = current.next
                return True
            else:
                return self.remove(value, current.next, current)
        return False

    def contains(self, value, current=None):
        """Check if the list contains the value recursively."""
        if current is None:
            current = self.__head
        if current:
            if current.data == value:
                return True
            return self.contains(value, current.next)
        return False

    def insert(self, value, index, current=None, counter=0):
        """Insert value at the specified index in the list recursively."""
        if current is None:
            current = self.__head
            if index == 0:
                self.__head = Node(value)
                self.__head.next = current
                return
        else:
            if counter == index - 1:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                return
            elif current.next is None and counter < index - 1:
                current.next = Node(value)  # Insert at the end if index is out of bounds
                return
            self.insert(value, index, current.next, counter + 1)

    def reverse(self, current=None, previous=None):
        """Reverse the list recursively without changing node data."""
        if current is None:
            current = self.__head
            if current is None:
                return
            self.__head = None
        next_node = current.next
        current.next = previous
        if next_node is None:
            self.__head = current
            return
        self.reverse(next_node, current)

    def to_plain_list(self, current=None):
        """Create a plain Python list from the linked list recursively."""
        if current is None:
            current = self.__head
            return [] if current is None else self.to_plain_list(current)
        else:
            return [current.data] + self.to_plain_list(current.next)

