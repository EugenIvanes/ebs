
from turtle import back
from django.db import models
from django.forms import DateTimeField
from apishop.models import Products
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100,null=True)

    def __str__(self):
        return str(self.id)
class OrderItem(models.Model):
    product = models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    data_added = models.DateTimeField(auto_now_add=True)
class ShippingAddress(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=50,null=False)
    city = models.CharField(max_length=50,null=False)
    state = models.CharField(max_length=50,null=False)
    zipcode = models.CharField(max_length=50,null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address