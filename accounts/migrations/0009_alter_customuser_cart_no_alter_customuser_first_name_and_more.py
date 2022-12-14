# Generated by Django 4.1.1 on 2022-10-24 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_customuser_cart_no_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cart_no',
            field=models.CharField(blank=True, max_length=50, verbose_name='cart number'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='p_id',
            field=models.CharField(blank=True, max_length=50, verbose_name='personal id'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_no',
            field=models.CharField(blank=True, max_length=50, verbose_name='phone number'),
        ),
    ]
