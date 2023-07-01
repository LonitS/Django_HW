from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    currency_type = models.CharField(max_length=3)
    created = models.DateTimeField()
    source = models.CharField(max_length=70)


class ContactUS(models.Model):
    email_from = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField()
