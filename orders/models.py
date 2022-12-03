from django.db import models
from django.conf import settings

# Create your models here.

class Orders(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Orders')
    is_paid = models.BooleanField(default=False)

    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    address = models.CharField(max_length=700)
    order_note = models.TextField(blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='Orders' )
    product = models.ForeignKey('product.Product', on_delete=models.DO_NOTHING, related_name='OrderItem')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'Order Item {self.id}'


