from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import RateForm, SourceForm

# from currency.models import Rate
import currency.models as models


def hello_world(request):
    return HttpResponse('Hello world!!')


def rate_list(request):
    data = models.Rate.objects.all()
    context = {
        'data': data
    }
    return render(request, 'rate_list.html', context)


def rate_create(request):
    if request.method == 'POST':
        form = RateForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/rate_list/')

    elif request.method == 'GET':
        form = RateForm()
    context = {'form': form}
    return render(request, 'rate_create.html', context)


def rate_update(request, pk):
    rate = get_object_or_404(models.Rate, pk=pk)

    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/rate_list/')

    elif request.method == 'GET':
        form = RateForm(instance=rate)
    context = {'form': form}
    return render(request, 'rate_create.html', context)


def rate_delete(request, pk):
    rate = get_object_or_404(models.Rate, pk=pk)
    if request.method == 'GET':
        context = {'data': rate}
        return render(request, 'rate_delete.html', context)
    elif request.method == 'POST':
        rate.delete()
        return HttpResponseRedirect('/rate_list/')


def rate_details(request, pk):
    data = get_object_or_404(models.Rate, pk=pk)
    context = {'data': data}
    return render(request, 'rate_details.html', context)


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


def source_list(request):
    data = models.Source.objects.all()
    context = {
        'data': data
    }
    return render(request, 'source_list.html', context)


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/source_list/')

    elif request.method == 'GET':
        form = SourceForm()
    context = {'form': form}
    return render(request, 'source_create.html', context)


def source_update(request, pk):
    data = get_object_or_404(models.Source, pk=pk)

    if request.method == 'POST':
        form = SourceForm(request.POST, instance=data)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/source_list/')

    elif request.method == 'GET':
        form = SourceForm(instance=data)
    context = {'form': form}
    return render(request, 'source_create.html', context)


def source_delete(request, pk):
    data = get_object_or_404(models.Source, pk=pk)
    if request.method == 'GET':
        context = {'data': data}
        return render(request, 'source_delete.html', context)
    elif request.method == 'POST':
        data.delete()
        return HttpResponseRedirect('/source_list/')


def source_details(request, pk):
    data = get_object_or_404(models.Source, pk=pk)
    context = {'data': data}
    return render(request, 'source_details.html', context)
