from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=30)
    thumbnail = models.ImageField()
    price = models.IntegerField()
    offer_price = models.IntegerField()
    slug = models.SlugField()
    # categorys = models.ForeignKey(on_delete=models.CASCADE)
    tags = models.TextField()
    quantity = models.IntegerField()


    def __str__(self):
        return f'{self.name},{self.tags}'

class order(models.Model):
    user = models.ForeignKey(product,related_name = 'users',on_delete = models.CASCADE,null=True,blank=True)
    productss = models.ForeignKey(product,related_name = 'Product', on_delete = models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField()
    ordered_at = models.CharField(max_length=30)
    is_completed = models.BooleanField()

    def __str__(self):
        return f'{self.user},{self.productss}'

class cart(models.Model):
    user = models.ForeignKey(product, related_name = 'userss',on_delete=models.CASCADE,null=True,blank=True)
    products = models.ForeignKey(order,related_name = 'Products',on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField()
    is_checked = models.BooleanField()

    def __str__(self):
        return f'{self.user},{self.products}'

class category(models.Model):
    categorys = models.ForeignKey(product,related_name = 'Category',on_delete=models.CASCADE,null=True,blank=True)
    slug = models.SlugField()

    def __str__(self):
        return f'{self.categorys}'

