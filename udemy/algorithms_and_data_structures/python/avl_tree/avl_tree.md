
#### Sources : Algorithms and Data Structures in Python (by Holczer Balazs on Udemy)
<br>

---

## __AVL Tree__
<br>

### __1) Overview and Characteristics__
<br>

* It is a balanced data structure invented back in 1962 by Adelson-Velsky and Landis (AVL)

* This data structure has a guaranteed O(logN) running time

* The running time of binary search trees depends on the h height of the binary search tree

* All the operations are the same as we have seen with binary search trees (insertion and removal)

* After every insertion and removal operations, we have to check whether the tree has become imbalanced or not

* If the tree is imbalanced then we have to make rotations

* height = max( left child’s height , right child’s height ) + 1

* balance factor = left child's height - right child's height
