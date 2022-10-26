
#### Sources : Algorithms and Data Structures in Python (by Holczer Balazs on Udemy)
<br>

---

## __AVL Tree__
<br>

### __1) Overview and Characteristics__
<br>

* It is a balanced data structure invented back in 1962 by Adelson-Velsky and Landis (AVL)

* This data structure has a guaranteed $ O(logN) $ running time

* The running time of binary search trees depends on the h height of the binary search tree

* All the operations are the same as we have seen with binary search trees (insertion and removal)

* After every insertion and removal operations, we have to check whether the tree has become imbalanced or not

* If the tree is imbalanced then we have to make rotations

* $ height = max(\text{left child’s height}, \space \text{right child’s height}) + 1 $

* $ balance \space factor = \text{left child's height} - \text{right child's height} $

<br>

### __2) AVL Tree Rotations__
<br>

* We have to track the h height parameters for all the nodes in the binary search tree

* Calculate the balance factors for the nodes to make rotations if necessary to rebalance search trees

* Left rotations - negative balance factors mean right heavy situation so we have to make a left rotation to rebalance the tree

* Right rotations - positive balance factors mean left heavy situation so we have to make a right rotation to rebalance the tree

* Rotations are extremely fast – we just have to update the references in $ O(1) $ constant running time

* This operation does not change the properties of the tree

* There may be other issues because of rotations

* We have to check up to the root node whether to make further rotations or not – it takes $ O(logN) $ running time

---