# Generated by Django 3.2 on 2022-06-02 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shop.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='product name')),
                ('thumbnail', models.ImageField(upload_to=shop.utils.upload_image_path, verbose_name='product thumbnail')),
                ('description', models.TextField(verbose_name='product description')),
                ('price', models.IntegerField(verbose_name='product price')),
                ('offer_price', models.IntegerField(blank=True, null=True, verbose_name='product offer price')),
                ('slug', models.SlugField(editable=False, unique=True, verbose_name='product slug')),
                ('tags', models.TextField(blank=True, null=True, verbose_name='product tags')),
                ('quantity', models.IntegerField(default=1, verbose_name='product quantity')),
                ('featured', models.BooleanField(default=False, verbose_name='featured product')),
                ('active', models.BooleanField(default=True, verbose_name='active product')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='product category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='order quantity')),
                ('is_shipped', models.BooleanField(default=False, verbose_name='shipped')),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.product', verbose_name='order product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='order user')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='cart quantity')),
                ('is_checked_out', models.BooleanField(default=False, verbose_name='checked out')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='cart product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='cart user')),
            ],
        ),
    ]
