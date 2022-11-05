
#### Sources : Algorithms and Data Structures in Python (by Holczer Balazs on Udemy)
<br>

---

## __Red-Black Tree__
<br>

### __1) Overview and Characteristics__
<br>

* This data structure has a guaranteed $ O(logN) $ running time

* AVL trees are faster than red-black trees because they are more rigidly balanced but needs more work, however, it is faster to construct a red-black tree

* Each node is either red or black 

* The root node is always black

* All lead nodes (NULL pointers) are black

* Every red node must have two black child nodes and no other children – it must have a black parent

* Every path from a given node to any of its descendant NULL nodes contains the same number of black nodes

<br>

### __2) Red-black Tree Rotations__

* We have to track the red-black properties for all the nodes in the binary search tree and make rotations if necessary to rebalance search trees

* Left rotations - negative balance factors means right heavy situation so we have to make a left rotation to rebalance the tree

* Right rotations - positive balance factors means left heavy situation so we have to make a right rotation to rebalance the tree

<br>

### __3) Time Complexity Comparison__
<br>

| Operations         | Average-Case | Worst-Case |
|--------------------|--------------|------------|
| space complexity   | $ O(N) $     | $ O(N) $   |
| insertion          | $ O(logN) $  | $ O(N) $   |
| deletion (removal) | $ O(logN) $  | $ O(N) $   |
| search             | $ O(logN) $  | $ O(N) $   |

---
