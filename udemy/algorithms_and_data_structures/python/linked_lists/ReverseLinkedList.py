
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

    def reverse(self):
        current_node = self.head
        previous_node = None
        next_node = None

        while current_node is not None:
            next_node = current_node.next_node
            # swap pointers
            current_node.next_node = previous_node
            # be ready for the next step
            previous_node = current_node
            current_node = next_node

        # set up head
        self.head = previous_node

    def insert(self, data):
        self.node_length += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def traverse_list(self):
        actual_node = self.head

        while actual_node is not None:
            print(f'{actual_node.data}')
            actual_node = actual_node.next_node


if __name__ == '__main__':

    linked_list = LinkedList()

    for i in range(10000000):
        linked_list.insert(i)
        
    start_time = time.time()
    linked_list.reverse()
    end_time = time.time()
    print(f'{round(end_time - start_time, 5)}')
    # 0.47918