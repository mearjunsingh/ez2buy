# Generated by Django 3.2 on 2022-03-18 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_order_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]