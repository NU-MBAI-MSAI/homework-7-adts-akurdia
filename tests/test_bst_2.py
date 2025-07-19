from unittest import TestCase
from p2.bst import BST


class TestBST2(TestCase):

    def test_inorder_traversal1(self):
        pass
        # nodes = [63, 29, 89, 15, 10, 24, 77, 95, 99]
        # tree = BST.create(nodes)
        # self.assertEqual([10, 15, 24, 29, 63, 77, 89, 95, 99], tree.traverse_inorder())

    def test_inorder_traversal2(self):
        pass
        # nodes = [25, 20, 15, 30, 22, 35, 29]
        # tree = BST.create(nodes)
        # self.assertEqual([15, 20, 22, 25, 29, 30, 35], tree.traverse_inorder())

    def test_breadth_first_traversal1(self):
        pass
        # nodes = [63, 29, 89, 15, 10, 24, 77, 95, 99]
        # tree = BST.create(nodes)
        # self.assertEqual([63, 29, 89, 15, 77, 95, 10, 24, 99], tree.breadth_first_traversal())

    def test_breadth_first_traversal2(self):
        pass
        # nodes = [25, 20, 15, 30, 22, 35, 29]
        # tree = BST.create(nodes)
        # self.assertEqual([25, 20, 30, 15, 22, 29, 35], tree.breadth_first_traversal())
