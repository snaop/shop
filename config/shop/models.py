from django.db import models


class Product (models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="images/Product/")
    desc = models.TextField()
    price = models.FloatField()
    discount = models.PositiveBigIntegerField()
    stock = models.PositiveBigIntegerField()
    is_available = models.BooleanField(default= True)


class Order (models.Model):
    product = models.ForeignKey(Product, on_delete= models.SET_NULL, null = True)
    delivery_adress = models.CharField(max_length = 250)
    created_at = models.DateTimeField(auto_now_add= True)
    