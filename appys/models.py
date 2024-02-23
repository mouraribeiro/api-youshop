from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField()
    active = models.BooleanField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    joined = models.DateTimeField(null=True, blank=True)
    accounts = models.ForeignKey(Account, on_delete=models.CASCADE)


class Tree(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Location(models.Model):
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)


class Plant(models.Model):
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    age = models.IntegerField()
    planted_at = models.DateTimeField()
    done = models.BooleanField()

    def __str__(self):
        return self.tree.name
