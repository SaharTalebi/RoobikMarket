# Generated by Django 4.1.1 on 2022-10-29 09:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0002_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user_wishlist',
            field=models.ManyToManyField(blank=True, related_name='user_wishlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
