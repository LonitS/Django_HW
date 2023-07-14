from django.urls import path

import currency.views as views

app_name = 'currency'

urlpatterns = [

    path('rate/list/', views.RateListView.as_view(), name='rate_list'),
    path('rate/create/', views.RateCreateView.as_view(), name='rate_create'),
    path('rate/update/<int:pk>/', views.RateUpdateView.as_view(), name='rate_update'),
    path('rate/details/<int:pk>/', views.RateDetailView.as_view(), name='rate_details'),
    path('rate/delete/<int:pk>/', views.RateDeleteView.as_view(), name='rate_delete'),

    path('source/list/', views.SourceListView.as_view(), name='source_list'),
    path('source/create/', views.SourceCreateView.as_view(), name='source_create'),
    path('source/update/<int:pk>/', views.SourceUpdateView.as_view(), name='source_update'),
    path('source/delete/<int:pk>/', views.SourceDeleteView.as_view(), name='source_delete'),
    path('source/details/<int:pk>/', views.SourceDetailView.as_view(), name='source_details'),

]
