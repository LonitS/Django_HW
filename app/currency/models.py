from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(max_length=3)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=70)

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
