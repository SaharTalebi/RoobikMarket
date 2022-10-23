from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.

class PersonalInfo(models.Model):
    person = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    p_id = models.CharField(max_length=20)
    cart_number = models.CharField(max_length=30)

    def __str__(self):
        return self.person.email

