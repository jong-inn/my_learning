

#### Sources : Algorithms and Data Structures in Python (by Holczer Balazs on Udemy)
<br>

---

## __Doubly_Linked Lists__
<br>

### __1) Overview and Characteristics__
<br>

* Every node stores the data itself and a reference to the next node and the previous node in the linked list

* Need more memory thand linked list

<br>

### __2) Advantages and Disadvantages__
<br>

* Advantage 1: We store references to the head node and the tail node as well so these nodes can be accessed in O(1) running time

* Advantage 2: It can be traversed in both directions

* Advantage 3: Removing a given node is easier because there is a pointer to the previous node as well

* Disadvantage 1: Need more memory because of the references

* Disadvantage 2: A bit more complicated to implement because we have to handle both of the pointers

* Disadvantage 3: Still have not solved the main issue – how to search for arbitrary items faster than O(N) linear running time?

---