

#### Sources : Algorithms and Data Structures in Python (by Holczer Balazs on Udemy)
<br>

---

## __Array__
<br>

### __1) Overview and Characteristics__
<br>

* Arrays are data structures where all the items are identified by an index – an integer starting with 0

* The items of the array are located right next to each other in the main memory (RAM) – they can be accessed by the index

* Random access: Items are located right next to each other so we can get them with the help of the index – in O(1) running time

<br>

### __2) Operations__
<br>

* [1] Adding items: We can insert new items at the end of the data structure until the data structure is not full – __O(1)__ running time

* [1] Adding items: start with a small sized array __vs__ allocate a huge array at the beginning

* [1] Adding items: We have to resize the array often with __O(N)__ running time

* [2] Adding numbers to arbitrary positions: We want to insert the an item to an arbitrary position – __O(N)__ linear running time because the items must be shifted

* [3] Removing last item: Removing the last item of an array data structure is quite easy and fast operation – __O(1)__ running time

* [4] Removing item from arbitrary position: We usually do not know the index of the item we wan to remove - first we have to find the item in __O(N)__ running time then remove the item in __O(1)__ and finally have to shift the other items in __O(N)__

<br>

### __3) Advantages and Disadvantages__

* Advantages 1: The best feature of arrays is random access: We can access arbitrary items extremely fast with indexes

* Advantages 2: Quite an easy data structure: Easy to understand and easy to implement as well

* Advantages 3: Arrays are fast data structures in the main

* Advantages 4: Use arrays when you want to manipulate the last items of the data structure or you want to access items with known indexes

* Disadvantage 1: We have to know the number of items we want to store at compile-time: So it is not a dynamic data structure

* Disadvantage 2: Since it is not dynamic: Whenever the data structure is full, we have to resize it in __O(N)__ linear running time

* Disadvantage 3: We usually can not store items with different types in an array – of course Python is exception

---