from django.db import models


class RateCurrencyChoices(models.IntegerChoices):
    USD = 1, 'Dollar'
    EUR = 2, 'Euro'


'''
CURRENCY_DOLLAR = 1
CURRENCY_EURO = 2
CURRENCY_CHOICES = [
    (CURRENCY_EURO, "Euro"),
    (CURRENCY_DOLLAR, 'Dollar')
]
'''