# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/21/2024
# Description:

class Node:
    """Represents a node in a linked list.

    Attributes:
        data: The value stored in the node.
        next: The next node in the linked list, or None if this is the last node.
    """

    def __init__(self, value):
        """Initializes a Node with a given value.

        Args:
            value: The value to be stored in the node.
        """
        self.data = value
        self.next = None


class LinkedList:
    """Represents a singly linked list.

    Attributes:
        _head: The head node of the linked list, or None if the list is empty.
    """

    def __init__(self):
        """Initializes an empty linked list."""
        self._head = None

    def get_head(self):
        """Returns the head node of the list.

        Returns:
            The head node of the linked list.
        """
        return self._head

    def add(self, value):
        """Adds a new node with the given value to the end of the list.

        Args:
            value: The value to add to the list.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            self.rec_add(value, self._head)

    def rec_add(self, value, current_node):
        """Recursively adds a new node with the given value to the end of the list.

        Args:
            value: The value to add to the list.
            current_node: The current node being examined in the recursion.
        """
        if current_node.next is None:
            current_node.next = Node(value)
        else:
            self.rec_add(value, current_node.next)

    def remove(self, value):
        """Removes the first occurrence of a node with the given value from the list.

        Args:
            value: The value to remove from the list.
        """
        if self._head is None:
            return
        if self._head.data == value:
            self._head = self._head.next
        else:
            self.rec_remove(value, self._head)

    def rec_remove(self, value, current_node):
        """Recursively removes the first occurrence of a node with the given value from the list.

        Args:
            value: The value to remove from the list.
            current_node: The current node being examined in the recursion.
        """
        if current_node.next is None:
            return
        if current_node.next.data == value:
            current_node.next = current_node.next.next
        else:
            self.rec_remove(value, current_node.next)

    def contains(self, value):
        """Checks if the list contains a node with the given value.

        Args:
            value: The value to search for in the list.

        Returns:
            True if the list contains a node with the value, False otherwise.
        """
        return self.rec_contains(value, self._head)

    def rec_contains(self, value, current_node):
        """Recursively checks if the list contains a node with the given value.

        Args:
            value: The value to search for in the list.
            current_node: The current node being examined in the recursion.

        Returns:
            True if the current node or any node after it contains the value, False otherwise.
        """
        if current_node is None:
            return False
        elif current_node.data == value:
            return True
        else:
            return self.rec_contains(value, current_node.next)

    def insert(self, value, index):
        """Inserts a new node with the given value at the specified index in the list.

        Args:
            value: The value to insert into the list.
            index: The index at which to insert the new node.
        """
        if index == 0:
            new_node = Node(value)
            new_node.next = self._head
            self._head = new_node
        else:
            self.rec_insert(value, index, self._head)

    def rec_insert(self, value, index, current_node):
        """Recursively inserts a new node with the given value at the specified index in the list.

        Args:
            value: The value to insert into the list.
            index: The index at which to insert the new node, relative to the current node.
            current_node: The current node being examined in the recursion.
        """
        if current_node is None:
            return
        elif index == 1:
            new_node = Node(value)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            self.rec_insert(value, index-1, current_node.next)

    def reverse(self):
        """Reverses the linked list in place."""
        if self._head is None or self._head.next is None:
            return
        else:
            self.rec_reverse(self._head, None)

    def rec_reverse(self, current_node, prev_node):
        """Recursively reverses the linked list.

        Args:
            current_node: The current node being examined in the recursion.
            prev_node: The previous node in the recursion, or None if current_node is the head.
        """
        if current_node is None:
            self._head = prev_node
        else:
            next_node = current_node.next
            current_node.next = prev_node
            self.rec_reverse(next_node, current_node)

    def to_plain_list(self):
        """Converts the linked list to a plain Python list.

        Returns:
            A list containing the values of the nodes in the linked list.
        """
        if self._head is None:
            return []
        else:
            return [self._head.data] + self.rec_to_plain_list(self._head.next)

    def rec_to_plain_list(self, current_node):
        """Recursively converts the linked list to a plain Python list.

        Args:
            current_node: The current node being examined in the recursion.

        Returns:
            A list containing the values of the current node and all nodes after it in the list.
        """
        if current_node is None:
            return []
        else:
            return [current_node.data] + self.rec_to_plain_list(current_node.next)
