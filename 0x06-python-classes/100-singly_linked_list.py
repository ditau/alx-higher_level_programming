#!/usr/bin/python3
"""Define classes for a singly-linked list"""

class Node:
    """Represents a node in a singly-linked list"""
    
    def __init__(self, data, next_node=Node):
        """Initialize a new node
        Args:
            data (int): the data of the new node
            next_node (Node): The next node of the new node
    """
    self.data = data
    self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the node."""
        return (self.__data)

    @data.setter
    def data(self, value):
    if not isinstance(value, int):
        raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
    """Get the next_nodeof the node"""
    return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
    if not isinstance(value, Node) and value is not None:
        raise TypeError("next_node must be a node object")
        self.__next_node = value

class SinglyLinkedList:
    """A singly-linked list"""

    def __init__(self):
        """Ïnitialize a Singly-linked list"""
        self.__head = None

    def sorted_insert(self, value):
    """Insert anew node to the singly-linked list at the correct
    numerical position.
    Args:
        value (Node): The  new node to insert
    """
    new = node(value)
    if self.__head is None:
        new.next_node = None
        self.__head = new
    elif self.__head.data > value:
        new.next_node = self.__head
        self.__head = new
    else:
        tmp = self.__head
        while (tmp.next_node is not None and
        tmp.next_node.data < value):
        new.next_node = tmp.next_node
        tmp.next_node = new

    def __str__(self):
        """print() representation of a SinglyLinkedList"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
            return ('\n'.join(values))
