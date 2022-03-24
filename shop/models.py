from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=80)
    thumbnail = models.ImageField()
    price = models.IntegerField()
    offer_price = models.IntegerField()
    slug = models.SlugField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    tags = models.TextField()
    quantity = models.IntegerField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)
    address = models.TextField()
    is_completed = models.BooleanField()

    def __str__(self):
        return f"Order - {self.product} - {self.user}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_checked_out = models.BooleanField()

    def __str__(self):
        return f"Cart - {self.product} - {self.user}"


class Category(models.Model):
    category = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.category


class SliderImage(models.Model):
    pass