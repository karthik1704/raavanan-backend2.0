from django.db import models
from treebeard.mp_tree import MP_Node


# Create your models here.
class Category(MP_Node):
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    image = models.ImageField(upload_to=f"categories/", blank=True, null=True)

    node_order_by = ["name"]

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return "Category: {}".format(self.name)
