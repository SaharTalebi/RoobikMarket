from django.db import models

from accounts.models import CustomUser


class Address(models.Model):
    IS_SELECTED_CHOICES = [
        ('true', 'بله'),
        ('false', 'خیر'),
    ]
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='Addresses', verbose_name='کاربر')
    state = models.CharField('استان', max_length=20)
    city = models.CharField('شهر', max_length=20)
    postal_code = models.CharField('کد پستی', max_length=20)
    full_address = models.CharField('آدرس کامل', max_length=300)
    phone_no = models.CharField('شماره تماس', max_length=20)
    # phone_no = models.BigIntegerField('شماره تماس', null=True, blank=True, validators=[
    #     validators.RegexValidators(r'^989[0-3,9]\d{8}$', 'Enter a valid mobile number')])
    delivery_person = models.CharField('تحویل گیرنده', max_length=100)

    is_selected = models.CharField('آدرس پیش فرض', max_length=6, choices=IS_SELECTED_CHOICES)

    def __str__(self):
        return self.person.email

    def delete_address(self):
        self.delete