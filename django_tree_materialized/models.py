import os
import re

from django.conf import settings
from django.db import models


class TreeMP(models.Model):
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    level = models.IntegerField(null=True)
    path = models.CharField(null=True, max_length=1024)

    @classmethod
    def number_to_str(cls, num):
        tree_mp_steplen = getattr(settings, 'TREE_MP_STEPLEN', 6)
        chars = "0123456789abcdefghijklmnopqrstuvwxyz"

        s = ""
        while num:
            s = chars[num % len(chars)] + s
            num //= len(chars)

        return str(s).rjust(tree_mp_steplen, '0')

    @classmethod
    def str_to_number(cls, num_str):
        chars = "0123456789abcdefghijklmnopqrstuvwxyz"
        num = 0
        for i, c in enumerate(reversed(num_str)):
            num += chars.index(c) * (len(chars) ** i)
        return num

    # Create node
    @classmethod
    def create(cls, parent=None, **kwargs) -> 'self':

        obj = cls.objects.create(**kwargs)
        obj.level = 1

        if parent:
            obj.parent = parent
            obj.level = parent.level + 1
            obj.path = obj.parent.path + cls.number_to_str(obj.id)
        else:
            obj.path = cls.number_to_str(obj.id)

        obj.save()
        return obj
