from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "contact us" 

    def __str__(self):
        return self.name
