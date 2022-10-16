
# Sources : Algorithms and Data Structures in Python (by Holczer Balazs on Udemy)

import time

class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.node_length = 0

    # O(1)
    def insert_start(self, data):

        self.node_length += 1
        new_node = Node(data)

        # the head is NULL (so the data structure is empty)
        if not self.head:
            self.head = new_node
        # there is at lest one item in the linked list
        else:
            new_node.next_node = self.head
            self.head = new_node

    # O(N)
    def insert_end(self, data):

        self.node_length += 1
        new_node = Node(data)

        actual_node = self.head

        # we have to find the end of the linked list in O(N) linear running time
        while actual_node.next_node is not None:
            actual_node = actual_node.next_node

        # actual_node is the last node: so we insert the new_node right after the actual_node
        actual_node.next_node = new_node

    # O(1)
    def size_of_list(self):
        return self.node_length

    # have to consider all the items in O(N) linear running time
    def traverse(self):

        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node

    # O(N) linear running time for finding arbitrary item
    def remove(self, data):

        # list is empty
        if self.head is None:
            return

        actual_node = self.head
        # we have to track the previous node for future pointer updates
        previous_node = None

        # search for the item we want to remove
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        # search miss
        if actual_node is None:
            return

        # the head node is the one we want to remove
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            # remove an internal node by updating the pointers
            # NO NEED TO del THE NODE BECAUSE THE GARBAGE COLLECTOR WILL DO THAT
            previous_node.next_node = actual_node.next_node


if __name__ == '__main__':

    linked_list = LinkedList()

    start_time = time.time()
    for i in range(100000):
        linked_list.insert_start(i)
    end_time = time.time()
    print(f'insert_start : {round(end_time - start_time, 10)}')
    # 0.0605046749
    
    start_time = time.time()
    for i in range(100000, 110000):
        linked_list.insert_end(i)
    end_time = time.time()
    print(f'insert_end : {round(end_time - start_time, 10)}')
    # 35.424380064

    start_time = time.time()
    for i in [1999, 2050, 15000, 90000, 105000]:
        linked_list.remove(i)
    end_time = time.time()
    print(f'remove arbitrary : {round(end_time - start_time, 10)}')
    # 0.0188732147
