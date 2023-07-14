# from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.urls import reverse_lazy


import currency.forms as forms
import currency.models as models


class RateListView(ListView):
    queryset = models.Rate.objects.all()
    template_name = 'rate_list.html'


class RateCreateView(CreateView):
    form_class = forms.RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy('currency:rate_list')


class RateUpdateView(UpdateView):
    model = models.Rate
    form_class = forms.RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy('currency:rate_list')


class RateDetailView(DetailView):
    model = models.Rate
    template_name = 'rate_details.html'


class RateDeleteView(DeleteView):
    model = models.Rate
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate_list')


class SourceListView(ListView):
    queryset = models.Source.objects.all()
    template_name = 'source_list.html'


class SourceCreateView(CreateView):
    form_class = forms.SourceForm
    template_name = 'source_create.html'
    success_url = reverse_lazy('currency:source_list')


class SourceUpdateView(UpdateView):
    model = models.Source
    form_class = forms.SourceForm
    template_name = 'source_create.html'
    success_url = reverse_lazy('currency:source_list')


class SourceDetailView(DetailView):
    model = models.Source
    template_name = 'source_details.html'


class SourceDeleteView(DeleteView):
    model = models.Source
    template_name = 'source_delete.html'
    success_url = reverse_lazy('currency:source_list')


class IndexView(TemplateView):
    template_name = 'index.html'


def contact_us(request):
    data = models.ContactUS.objects.all()
    context = {
        'data': data
    }
    return render(request, 'contact_us.html', context)
