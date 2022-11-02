from django.db import models

from accounts.models import CustomUser


class Address(models.Model):
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='Addresses')
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20)
    full_address = models.CharField(max_length=300)
    phone_no = models.CharField(max_length=20)
    delivery_person = models.CharField(max_length=100)

    def __str__(self):
        return self.person.email

    def delete_address(self):
        self.delete