
# Sources : Algorithms and Data Structures in Python (by Holczer Balazs on Udemy)

import time

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # this operation inserts items at the end of the linked list
    # so we have to manipulate the tail node in O(1) running time
    def insert(self, data):

        new_node = Node(data)

        # when the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # there is at least 1 item in the data structure
        # we keep inserting items at the end of the linked list
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # we can traverse a doubly linked list in both directions
    def traverse_forward(self):

        actual_node = self.head

        while actual_node is not None:
            print(f'{actual_node.data}')
            actual_node = actual_node.next

    def traverse_backward(self):

        actual_node = self.tail

        while actual_node is not None:
            print(f'{actual_node.data}')
            actual_node = actual_node.previous


if __name__ == '__main__':

    linked_list = DoublyLinkedList()
    
    for i in range(10000):
        linked_list.insert(i)
    
    
    start_time = time.time()
    linked_list.traverse_forward()
    end_time = time.time()
    print(f'{round(end_time - start_time, 5)}')
    # 0.00025

    start_time = time.time()
    linked_list.traverse_backward()
    end_time = time.time()
    print(f'{round(end_time - start_time, 5)}')
    # 0.00025
    