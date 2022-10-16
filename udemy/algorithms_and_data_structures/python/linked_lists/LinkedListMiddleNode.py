
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

    # O(N) linear running time complexity
    def get_middle_node(self):

        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            # go 2 times faster than slow pointer
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        return slow_pointer

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
            print(f"{actual_node.data}")
            actual_node = actual_node.next_node


if __name__ == '__main__':

    linked_list = LinkedList()

    for i in range(1000000):
        linked_list.insert(i)

    start_time = time.time()
    print(linked_list.get_middle_node().data)
    end_time = time.time()
    
    print(f'{round(end_time - start_time, 5)}')
    # 0.05292
