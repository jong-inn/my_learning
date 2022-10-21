
#### Sources : Algorithms and Data Structures in Python (by Holczer Balazs on Udemy)
<br>

---

## __Binary Search Tree__
<br>

### __1) Overview and Characteristics__
<br>

* Every node in the tree can have at most 2 children (left child and right child)

* Left child is smaller than the parent node

* Right child is greater than the parent node

* We can access the root node exclusively and all other nodes can be accessed via the root node

* The height of a tree is the number of edges on the longest downward path between the root and a leaf node. The number of layers the tree contains.

* How many N nodes are there in a complete binary search tree with h height?
<br>
N = 2^(h-1)

* The logarithmic O(logN) running time is valid only when the tree structure is balanced

* It keeps the keys in sorted order so that lookup and other operations can use the principle of binary search with O(logN) running time

<br>

### __2) Operations__
<br>

[1] Search Max: The maximum item in the binary search tree is the rightmost item in the tree

[2] Search Min: The minimum item in the binary search tree is the leftmost item in the tree

[3] Removing a leaf node: We just have to notify the parent that the child has been removed

[4] Removing a node with a single child: We just have to notify the parent that the left (or right) child has been changed

[5] Removing a node with two children: Find a predecessor node and replace with that node

[6] Pre-order traversal: We visit the root node of the binary tree then the left subtree and finally the right subtree in a recursive manner

[7] Post-order traversal: We visit the left subtree of the binary tree then the right subtree and finally the root node in a recursive manner

[8] In-order traversal: We visit the left subtree of the binary tree then the root node and finally the right subtree in a recursive manner

<br>

### __3) Time Complexity Comparison__
<br>

| Operations         | Average-Case | Worst-Case |
|--------------------|--------------|------------|
| space complexity   | O(N)         | O(N)       |
| insertion          | O(logN)      | O(N)       |
| deletion (removal) | O(logN)      | O(N)       |
| search             | O(logN)      | O(N)       |

---