from django.db import models

# Create your models here.


class Concert(models.Model):
    date = models.DateTimeField()
    venue = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50)
    tickets = models.CharField(max_length=300, null=False)

