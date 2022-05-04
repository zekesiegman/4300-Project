from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=1)
    cardNumber = models.CharField(max_length=500, default='')
    expiration = models.DateField(default=django.utils.timezone.now)
    billingAddress = models.CharField(max_length=250, default='')

    def __str__(self) :
        return self.user.name


class Item(models.Model):
    itemId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    url = models.URLField()
    price = models.IntegerField()
    storage = models.IntegerField()
    ram = models.IntegerField()
    camera_res = models.IntegerField()
    size = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name


class Cart(models.Model):
    cartItemId = models.AutoField(primary_key=True, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item = models.ForeignKey('Item', on_delete=models.CASCADE, default=1)
    copies = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.cartItemId + ' ' + self.user.name