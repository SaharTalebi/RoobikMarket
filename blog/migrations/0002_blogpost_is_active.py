# Generated by Django 4.1.1 on 2022-09-12 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
