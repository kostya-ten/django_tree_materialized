from django.db import models
from django_tree_materialized.models import TreeMP


class Tree(TreeMP):
    name = models.CharField(max_length=200)
