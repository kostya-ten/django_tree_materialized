from django.test import TestCase
from . import models


class Tree(TestCase):
    def test_number_to_str(self):
        self.assertEqual(models.Tree.number_to_str(1234567890), 'kf12oi')
        self.assertEqual(models.Tree.str_to_number('kf12oi'), 1234567890)

        self.assertEqual(models.Tree.number_to_str(65), '00001t')
        self.assertEqual(models.Tree.str_to_number('00001t'), 65)

    def test_create_node(self):
        tree = models.Tree.create(name="Name node")
        self.assertEqual(tree.name, 'Name node')
        self.assertEqual(tree.level, 1)
        self.assertIsNone(tree.parent)
        self.assertEqual(tree.path, '000001')

    def test_create_node_child(self):
        parent_tree = models.Tree.create(name="Name node parent")

        self.assertEqual(parent_tree.name, 'Name node parent')
        self.assertEqual(parent_tree.level, 1)
        self.assertIsNone(parent_tree.parent)
        self.assertEqual(parent_tree.path, '000001')

        child_tree = models.Tree.create(name="Name node child", parent=parent_tree)
        self.assertEqual(child_tree.name, 'Name node child')
        self.assertEqual(child_tree.level, 2)
        self.assertIsNot(child_tree.parent, None)
        self.assertEqual(child_tree.path, '000001000002')

    def test_create_node_child_multi(self):
        parent_tree = models.Tree.create(name="Name node parent")

        for item in range(0, 20):
            child_tree = models.Tree.create(name="Name node child", parent=parent_tree)
            self.assertEqual(child_tree.level, 2)
            self.assertRegex(child_tree.path, '^000001')

    def test_mobile_number(self):
        tree = models.Tree.create(name="Костя")
        # print(tree.level, tree.path)

        for i in range(1, 15):
            tree = models.Tree.create(name='test', parent=tree)
            # print(tree.level, tree.path)

        # models.Tree.delete(obj=3)

        res = models.Tree.objects.all()
        for i in res:
            if i.parent:
                print(i.level, i.parent.id, i.path)
            else:
                print(i.level, None, i.path)



        self.assertEqual(1, 1)
