from django.test import TestCase
from . import models


class Tests(TestCase):
    def test_number_to_str(self):
        result = models.Tree.number_to_str(1)
        self.assertEqual(result, "000001")

        result = models.Tree.number_to_str(100)
        self.assertEqual(result, "00002s")

    def test_str_to_number(self):
        result = models.Tree.str_to_number("000001")
        self.assertEqual(result, 1)

        result = models.Tree.str_to_number("00002s")
        self.assertEqual(result, 100)

    def test_create(self):
        tree = models.Tree.create(name="Name node")
        self.assertEqual(tree.level, 1)
        self.assertEqual(tree.path, "000001")

    def test_sub_create(self):
        tree = models.Tree.create(name="Name node")
        tree_sub = models.Tree.create(name="Name node", parent=tree)

        self.assertEqual(tree_sub.level, 2)
        self.assertEqual(tree_sub.path, "000001000002")

    def test_get_family(self):
        tree = models.Tree.create(name="Name node1")
        tree_sub1 = models.Tree.create(name="Name node2", parent=tree)
        tree_sub2 = models.Tree.create(name="Name node3", parent=tree_sub1)

        result = tree_sub2.get_family()
        self.assertEqual(result.count(), 3)

        res_tree = result.filter(name="Name node1").get()
        self.assertEqual(res_tree.name, "Name node1")

        res_tree = result.filter(name="Name node2").get()
        self.assertEqual(res_tree.name, "Name node2")

        res_tree = result.filter(name="Name node3").get()
        self.assertEqual(res_tree.name, "Name node3")

    def test_get_children(self):
        tree = models.Tree.create(name="Name node1")
        models.Tree.create(name="Name node2", parent=tree)

        result = tree.get_children()
        self.assertEqual(result.count(), 2)

        res_tree = result.filter(name="Name node1").get()
        self.assertEqual(res_tree.name, "Name node1")

        res_tree = result.filter(name="Name node2").get()
        self.assertEqual(res_tree.name, "Name node2")
