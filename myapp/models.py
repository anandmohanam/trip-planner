
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Contact(models.Model):
    fullname = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)
    msg = models.CharField(max_length=20)


class Package(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField( null=True)
    image = models.ImageField(upload_to='package_image',null=True)
    price = models.IntegerField(null=True)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.title)

class Menu(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=30, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return str(self.title)