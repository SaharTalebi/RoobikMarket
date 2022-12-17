# Generated by Django 4.1.1 on 2022-12-04 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_address_is_selected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='is_selected',
            field=models.CharField(choices=[('true', 'بله'), ('false', 'خیر')], max_length=6),
        ),
    ]