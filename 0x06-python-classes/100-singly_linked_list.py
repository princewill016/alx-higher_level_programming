#!/usr/bin/python3
"""
Module that defines Node and SinglyLinkedList classes.
"""


class Node:
    """
    Class that defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node.

        Args:
            data (int): The data stored in the node.
            next_node (Node): The next node in the list (default is None).
        """
        self.data = data  # Use the setter to validate data
        self.next_node = next_node  # Use the setter to validate next_node

    @property
    def data(self):
        """
        Retrieve the data from the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data of the node with validation.

        Args:
            value (int): The data to set in the node.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next node.

        Returns:
            Node: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node with validation.

        Args:
            value (Node): The next node in the list.

        Raises:
            TypeError: If next_node is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class that defines a singly linked list.
    """

    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.__head = None

    def __str__(self):
        """
        Print the entire list, one node number per line.

        Returns:
            str: The string representation of the list.
        """
        node = self.__head
        values = []
        while node is not None:
            values.append(str(node.data))
            node = node.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list (in increasing order).

        Args:
            value (int): The value to insert in the list.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
