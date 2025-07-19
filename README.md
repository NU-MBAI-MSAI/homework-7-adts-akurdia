## Homework Instructions
MSAI 305 Intensive Program Design<br>


Test Instructions
---
- This homework uses the unittest testing framework instead of the pytest testing framework. 
- However, it behaves very similarly. At any point, you can run individual tests by clicking 
  on the green play button next to the tests. 
- You can also run all the tests by right-clicking on the runner.py and choosing Run. This will run all 
  the tests for all the problems and provide useful information.

Problem 1 - Binary Search Trees and Recursion
---
1. In the `p1` package, you have been provided with a module named `bst.py` that contains a
   `Node` class and a `BST` class to represent a binary search tree (bst). In addition, you 
   have also been provided with the `insert` method and the `create` method so that you can 
   create a bst. A small sample tree has been provided for you.
2. Write the method `traverse_pre` that does not take any arguments (only has the `self` parameter).
   This method should recursively traverse a binary search tree and return the list of nodes
   traversed in preorder (root-left-right).
   - You will need a helper (auxiliary) method so that you can pass in the root node to start 
     traversing the tree. The `traverse_pre` method should call the helper method. You can make
     this helper method a nested function and then you won't have to include the `self` paramter.
     See the `insert` method for an example.
   - The root of a `BST` is a `Node` that has the following attributes: `val` (the value
     of the node), `left` (the left child of the node), `right` (the right child of the node).
   - Uncomment the import at the top of the `test_bst.py` file and uncomment and run the tests in
     the file that begin with `test_pre...`. Remove the pass keyword.
3. Write the method `traverse_post` that does not take any arguments (only has the `self` parameter).
   This method should recursively traverse a binary search tree and return the list of nodes
   traversed in postorder (left-right-root).
   - You will need a helper (auxiliary) method so that you can pass in the root node to start 
    traversing the tree. The `traverse_post` method should call the helper method. You can make
    this helper method a nested function and then you won't have to include the `self` paramter.
    See the `insert` method for an example.
   - The root of a `BST` is a `Node` that has the following attributes: `val` (the value  of the node), 
     `left` (the left child of the node), `right` (the right child of the node). 
   - Uncomment and run the tests in the `test_bst.py` file that begin with `test_post...`. 
     Remove the pass keyword.

Problem 2 - Practice with Stacks, Queues, and BSTs
---
1. In the `p2` package, you have again been provided with a module named `bst.py` that contains a
   `Node` class and a `BST` class to represent a binary search tree (bst). In addition, you 
   have also been provided with the `insert` method and the `create` method so that you can 
   create a bst. A small sample tree has been provided for you.
2. Write the method `traverse_inorder` that does not take any arguments (only has the `self` parameter).
   This method should traverse a binary search tree using a stack/iteration and return the list of nodes
   traversed inorder (left-root-right).
   - Do not do this using recursion. Instead, you should use a stack and iteration. The import 
     needed for this has been provided for you at the top of the file. An `if __main__` block has been
     provided for you with a method call commented out.
   - Uncomment the tests in the file that begin with `test_inorder...`. Remove the pass keyword.
3. Write the method `breadth_first_traversal` that does not take any arguments (only has the `self` parameter).
   This method should traverse a binary search tree and return the list of nodes using breadth-first
   search traversal from the root node to the leaves. 
   - Do not use recursion. Instead, you should use a queue and iteration. The import 
      needed for this has been provided for you at the top of the file. An `if __main__` block has been
      provided for you with a method call commented out.
   - Uncomment and run the tests in the `test_bst.py` file that begin with `test_breadth...`. 
     Remove the pass keyword.



**Push your code to GitHub!**