# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length= 101)
    lastName = models.CharField(max_length= 101)
    email = models.CharField(max_length= 101, unique= True)
    password = models.CharField(max_length=101)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Item(models.Model):
    itemName = models.CharField(max_length= 101)
    creator = models.ForeignKey(User, related_name='creator')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Addition(models.Model):
    user = models.ForeignKey(User, related_name='additions') 
    item = models.ForeignKey(Item, related_name='additions')
    created_at= models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now=True) 