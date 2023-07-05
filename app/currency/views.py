from django.http.response import HttpResponse

# from currency.models import Rate
import currency.models as models


def hello_world(request):
    return HttpResponse('Hello world!!')


def rate_list(request):
    results = []
    rates = models.Rate.objects.all()

    for rate in rates:
        results.append(
            f'ID: {rate.id}, sell: {rate.sell}, buy: {rate.buy},'
            f' created: {rate.created}, type: {rate.currency_type},'
            f' source: {rate.source}'
        )

    return HttpResponse(str(results))


def contact_us(request):
    results = []
    rows = models.ContactUS.objects.all()

    for row in rows:
        results.append(
            f'ID: {row.id}, '
            f'email_from: {row.email_from}, '
            f'subject: {row.subject},'
            f' message: {row.message}'
        )

    return HttpResponse(str(results))
