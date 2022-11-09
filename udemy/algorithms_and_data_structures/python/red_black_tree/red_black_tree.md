
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

### __4) Insertion Cases__
<br>

* Case 1 __(before)__

![image](./red_black_tree_case1.png)

&ensp;&ensp; - The x node will be the root node
<br>
&ensp;&ensp; - And recolor the children of x to black
<br>
&ensp;&ensp; - We have to check the properties recursively starting with x up to the root node in $ O(logN) $ running time

<br>

* Case 1 __(after)__

![image](./red_black_tree_case1_after.png)

<br>

* Case 2 __(before)__

![image](./red_black_tree_case2.png)

&ensp;&ensp; - We have to make a left/right rotation on the parent of node x
<br>
&ensp;&ensp; - We have to check the properties recursively starting with x up to the root node in $ O(logN) $ running time

<br>

* Case 2 __(after)__

![image](./red_black_tree_case2_after.png)

<br>

* Case 3 __(before)__

![image](./red_black_tree_case3.png)

&ensp;&ensp; - We have to rotate the grandparent of node x to the right/left and recolor
<br>
&ensp;&ensp; - We have to check the properties recursively starting with x up to the root node in $ O(logN) $ running time

<br>

* Case 3 __(after)__

![image](./red_black_tree_case3_after.png)

<br>

* Case 4 __(before)__

![image](./red_black_tree_case4.png)

&ensp;&ensp; - We have to move node x to the grandparent and recolor the children of grandparent node
<br>
&ensp;&ensp; - We have to check the properties recursively starting with x up to the root node in $ O(logN) $ running time

<br>

* Case 4 __(after)__

![image](./red_black_tree_case4_after.png)

<br>

---
