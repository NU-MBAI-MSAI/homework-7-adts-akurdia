from unittest import TestCase
from p1.bst import BST


class TestBST(TestCase):

    def test_traverse_pre1(self):
        nodes = [63, 29, 89, 77, 15, 95, 99, 10, 24]
        tree = BST.create(nodes)
        self.assertEqual([63, 29, 15, 10, 24, 89, 77, 95, 99], tree.traverse_pre())

    def test_traverse_pre2(self):
        nodes = [45]
        tree = BST.create(nodes)
        self.assertEqual([45], tree.traverse_pre())

    def test_traverse_post1(self):
        nodes = [63, 29, 89, 77, 15, 95, 99, 10, 24]
        tree = BST.create(nodes)
        self.assertEqual([10, 24, 15, 29, 77, 99, 95, 89, 63], tree.traverse_post())

    def test_traverse_post2(self):
        nodes = [45]
        tree = BST.create(nodes)
        self.assertEqual([45], tree.traverse_post())
