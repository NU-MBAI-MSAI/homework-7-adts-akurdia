from queue import LifoQueue, Queue


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if other is None or not isinstance(other, Node):
            return False
        else:
            return self.val == other.val and self.left == other.left and self.right == other.right

    def __hash__(self):
        return hash(self.val)


class BST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, number):
        def insert_node(tree):
            if number < tree.val and tree.left is not None:
                insert_node(tree.left)
            elif number < tree.val:
                tree.left = Node(number)
            elif number > tree.val and tree.right is not None:
                insert_node(tree.right)
            elif number > tree.val:
                tree.right = Node(number)
        if self.root is None:
            self.root = Node(number)
        else:
            insert_node(self.root)

    def __eq__(self, other):
        return self.root == other.root

    @staticmethod
    def create(nodes):
        tree = BST()
        if nodes:
            tree.root = Node(nodes.pop(0))
            for node in nodes:
                tree.insert(node)
        return tree

    def traverse_inorder(self):
        if self.root is None:
            return []
        
        result = []
        stack = LifoQueue()
        current = self.root
        
        while current is not None or not stack.empty():
            # Reach the leftmost node
            while current is not None:
                stack.put(current)
                current = current.left
            
            # Process current node
            current = stack.get()
            result.append(current.val)
            
            # Move to right subtree
            current = current.right
        
        return result

    def breadth_first_traversal(self):
        if self.root is None:
            return []
        
        result = []
        queue = Queue()
        queue.put(self.root)
        
        while not queue.empty():
            current = queue.get()
            result.append(current.val)
            
            if current.left is not None:
                queue.put(current.left)
            if current.right is not None:
                queue.put(current.right)
        
        return result


if __name__ == '__main__':
    nodes = [7, 10, 5, 9, 3, 6]
    bst = BST.create(nodes)
    print(bst.traverse_inorder()) # -> Should be [3, 5, 6, 7, 9, 10]
    print(bst.breadth_first_traversal())  # -> Should be [7, 5, 10, 3, 6, 9]
