
# Sources : Algorithms and Data Structures in Python (by Holczer Balazs on Udemy)

CAPACITY = 10

# maximum heap (root node will be the largest item)
class Heap:
    
    def __init__(self):
        # this is the actual number of items in the data structure
        self.heap_size = 0
        # the underlying list data structure
        self.heap = [0] * CAPACITY
        
    def insert(self, item):
        
        # when the heap is full
        if self.heap_size == CAPACITY:
            return
        
        self.heap[self.heap_size] = item
        self.heap_size += 1
        
        # check the heap properties
        self.fix_up(self.heap_size - 1)
    
    # starting with the actual node we have inserted up to root node
    # we have to compare the values whether to make swap operations
    # it has O(logN) running time complexity
    def fix_up(self, index):
        
        # i, 2i+1, 2i+2
        parent_index = (index - 1) // 2
        
        # we consider all the items above till we hit the root node
        # if heap property if violated then we swap the parent-child
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.fix_up(parent_index)
            
    # peek function return with the max item in O(1)
    def get_max(self):
        return self.heap[0]
    
    # return the max and removes it as well
    # remove the root node of the heap
    def poll(self):
        
        max_item = self.get_max()
        
        # swap the root node with the last item and heapify
        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        self.heap_size -= 1
        
        # make sure the heap is heapify
        self.fix_down(0)
        
        return max_item
    
    # starting with the root node downwards untill the heap properties are no longer violated - O(logN)
    def fix_down(self, index):
        
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        
        # in a max heap the parent is always greater than the children
        largest_index = index
        
        # looking for the largest (parent or left node)
        if left_index < self.heap_size and self.heap[left_index] > self.heap[index]:
            largest_index = left_index
            
        # if the right child is greater than the left child: largest is the right child
        if right_index < self.heap_size and self.heap[right_index] > self.heap[largest_index]:
            largest_index = right_index
        
        # if the parent is larger than the children: it is a valid heap so we terminate the recursive function calls
        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.fix_down(largest_index)
        
        
        