

#### Sources : Algorithms and Data Structures in Python (by Holczer Balazs on Udemy)
<br>

---

## __Linked Lists__
<br>

### __1) Overview and Characteristics__
<br>

* Every node stores the data itself and a reference the next node in the linked list data structure

* The items are not stores next to each other in the memory, so there is no random indexing

<br>

### __2) Operations__
<br>

* [1] Adding items: We can insert items at the beginning of the data structure fast – O(1) running time

* [2] Removing last item: We can remove items at the beginning of the data structure fast – O(1) running time

* [3] Adding/Removing items at the end: It is a slow operation to insert items at the end – O(N) running time

<br>

### __3) Advantages and Disadvantages__
<br>

* Advantages 1: Linked lists are dynamic data structures: they can acquire memory at run-time by inserting new nodes

* Advantages 2: No need for resizing the data structures

* Advantages 3: Manipulating the first item is fast – O(1) running time

* Advantages 4: Linked lists can store different sized items – arrays assume the items have the exact same size

* Disadvantage 1: Need more memory because of the references

* Disadvantage 2: There is no random access - we can only access the first node (head node) of the linked list

* Disadvantage 3: We can not go backwards

* Disadvantage 4: Not predictable – the running time of the application relies heavily on the operations the users do

* Disadvantage 5: Still have not solved the main issue – how to search for arbitrary items faster than O(N) linear running time?

---