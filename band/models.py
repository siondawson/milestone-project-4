from django.db import models

# Create your models here.


class Concert(models.Model):
    date = models.DateTimeField()
    venue = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50)
    tickets = models.CharField(max_length=300, null=False)


class Enquiry(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(null=False, blank=False)