from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.FloatField()
    img = models.ImageField(upload_to='item_images')
    seller = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
