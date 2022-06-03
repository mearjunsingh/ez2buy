from django.contrib.auth import get_user_model
from django.db import models

from .utils import generate_unique_slug, upload_image_path

User = get_user_model()


class Category(models.Model):
    category = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.category


class Product(models.Model):
    name = models.CharField("product name", max_length=80)
    thumbnail = models.ImageField("product thumbnail", upload_to=upload_image_path)
    description = models.TextField("product description")
    price = models.IntegerField("product price")
    offer_price = models.IntegerField("product offer price", blank=True, null=True)
    slug = models.SlugField("product slug", unique=True, editable=False)
    category = models.ForeignKey(
        Category, verbose_name="product category", on_delete=models.CASCADE
    )
    tags = models.TextField("product tags", blank=True, null=True)
    quantity = models.IntegerField("product quantity", default=1)
    featured = models.BooleanField("featured product", default=False)
    active = models.BooleanField("active product", default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generate_unique_slug(Product, self.name)
        return super(Product, self).save(*args, **kwargs)


class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name="cart user", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, verbose_name="cart product", on_delete=models.CASCADE
    )
    quantity = models.IntegerField("cart quantity")
    is_checked_out = models.BooleanField("checked out", default=False)

    def __str__(self):
        return f"Cart - {self.product} in {self.user}'s"


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="order user", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, verbose_name="order product", on_delete=models.PROTECT
    )
    quantity = models.IntegerField("order quantity")
    is_shipped = models.BooleanField("shipped", default=False)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order - {self.product} by {self.user}"
