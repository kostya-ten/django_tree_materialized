from django.test import TestCase
from . import models


class Validators(TestCase):
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
