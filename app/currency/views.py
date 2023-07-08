from django.http.response import HttpResponse
from django.shortcuts import render

# from currency.models import Rate
import currency.models as models


def hello_world(request):
    return HttpResponse('Hello world!!')


def rate_list(request):
    rates = models.Rate.objects.all()
    context = {
        'rates': rates
    }
    return render(request, 'rate_list.html', context)


def contact_us(request):
    data = models.ContactUS.objects.all()
    context = {
        'data': data
    }
    return render(request, 'contact_us.html', context)


def test_template(request):
    name = request.GET.get('name')
    context = {
        'username': name
    }
    return render(request, 'test.html', context)
