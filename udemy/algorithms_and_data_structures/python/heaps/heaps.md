
#### Sources : Algorithms and Data Structures in Python (by Holczer Balazs on Udemy)
<br>

---

## __Pirority Queues__
<br>

### __1) Overview and Characteristics__
<br>

* It is a queue and abstract data type

* Every item has an additional property – the so-called priority value

* In a priority queue, an element with high priority is served before an element with lower priority

* It is usually implemented with heap data structures but it can be implemented with self balancing trees as well

* Sometimes we do not specify the priority, for example when implementing heap data structures

* The concept of priority queues naturally suggests a sorting algorithm where we have to insert all the elements to be sorted into a priority queue

<br>

## __Heaps__
<br>

### __1) Overview and Characteristics__
<br>

* Heaps are basically binary trees

* Two main binary heap types: min heap and max heap

* In a max heap the keys of parent nodes are always greater than or equal to those of the children. The highest key (max value) is in the root node.

* In a min heap the keys of parent nodes are less than or equal to those of the children and the lowest key (min item) is in the root node

<br>

### __2) Properties__
<br>

* Completeness: We construct the heap from left to right across each row – of course the last row may not be fully complete

* Every node can have 2 children

* There are indexes from root node and left to right

* The node with index $ i $ has left child with index $ 2i+1 $ and right child with index $ 2i+2 $
