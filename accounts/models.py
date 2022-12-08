from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # username = models.CharField(max_length=50, unique=False, blank=False)
    # email = models.EmailField(unique=True, blank=False)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone_no = models.CharField(verbose_name='phone number', max_length=50, blank=True)
    cart_no = models.CharField(verbose_name='cart number', max_length=50, blank=True)
    p_id = models.CharField(verbose_name='personal id', max_length=50, blank=True)

    def __str__(self):
        return self.username
