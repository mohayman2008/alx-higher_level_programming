#!/usr/bin/python3
"""Singly Linked List Implementaion
"""
class Node:
    """Node of a singly linked list of integers

    """
    def __init__(self, data, next_node=None):
        """Initialize the Node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value
    def __str__(self):
        """
        """
        return str(self.data)
    pass

class SinglyLinkedList:
    """
    """
    def __init__(self):
        """ Initialize the linked list
        """
        self.__head = None;
    def __str__(self):
        """Prints the elements of the list (one node per line)
        """
        string = ""
        if self.__head is not None:
            current = self.__head
            while current:
                string += str(current)
                current = current.next_node
                if current:
                    string += "\n"
        return string
    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        if self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
            return

        current = self.__head
        while current:
            if (current.next_node is None or current.next_node.data > value):
                new.next_node = current.next_node
                current.next_node = new
                break
            current = current.next_node
    pass
