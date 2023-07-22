from django.db import models
from currency.models_choices import RateCurrencyChoices


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=70)
    currency = models.PositiveSmallIntegerField(
        choices=RateCurrencyChoices.choices,
        default=RateCurrencyChoices.USD
    )

    def __str__(self):
        return f'{self.buy}' \
               f'{self.sell}' \
               f'{self.currency}' \
               f'{self.created}' \
               f'{self.source}'


class ContactUS(models.Model):
    email_from = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField()

    def __str__(self):
        return f'{self.email_from}' \
               f'{self.subject}' \
               f'{self.message}'


class Source(models.Model):
    name = models.CharField(max_length=64)
    source_url = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}' \
               f'{self.source_url}'
