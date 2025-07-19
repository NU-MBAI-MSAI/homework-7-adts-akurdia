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
        # This is a nested function - it's only needed inside this function.
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

    def traverse_pre(self):
        def traverse_pre_helper(node):
            if node is None:
                return []
            result = [node.val]
            result.extend(traverse_pre_helper(node.left))
            result.extend(traverse_pre_helper(node.right))
            return result
        
        return traverse_pre_helper(self.root)

    def traverse_post(self):
        def traverse_post_helper(node):
            if node is None:
                return []
            result = []
            result.extend(traverse_post_helper(node.left))
            result.extend(traverse_post_helper(node.right))
            result.append(node.val)
            return result
        
        return traverse_post_helper(self.root)


if __name__ == '__main__':
    nodes = [25, 20, 30, 29, 35, 15, 22]
    tree = BST.create(nodes)
    print(tree.traverse_pre()) # -> This should return the list [25, 20, 15, 22, 30, 29, 35]
    print(tree.traverse_post()) # -> This should return the list [15, 22, 20, 29, 35, 30, 25]
