# Generated by Django 4.1.1 on 2022-10-27 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_options_and_more'),
        ('dashboard', '0004_favorit_delete_personalinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorit',
            name='product',
        ),
        migrations.AddField(
            model_name='favorit',
            name='product',
            field=models.ManyToManyField(to='product.product'),
        ),
    ]
