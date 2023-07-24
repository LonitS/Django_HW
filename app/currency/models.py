from django.db import models
from currency.models_choices import RateCurrencyChoices
from django.utils.translation import gettext_lazy as _


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
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(_('Name'), max_length=128, default='default_value')
    reply_to = models.EmailField(_('Email'))
    subject = models.CharField(_('Subject'), max_length=128)
    body = models.TextField(_('Body'), blank=True)

    def __str__(self):
        return f'{self.reply_to}' \
               f'{self.subject}' \
               f'{self.created}' \
               f'{self.name}' \
               f'{self.body}'


class Source(models.Model):
    name = models.CharField(max_length=64)
    source_url = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}' \
               f'{self.source_url}'


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=255)
    request_method = models.CharField(max_length=255)
    time = models.IntegerField()

    def __str__(self):
        return f'{self.path}' \
               f'{self.request_method}' \
               f'{self.time}'

    @classmethod
    def create(cls, path, request_method, time):
        rq_rs_log = cls(
            path=path,
            request_method=request_method,
            time=time

        )
        # do something with the book
        return rq_rs_log
