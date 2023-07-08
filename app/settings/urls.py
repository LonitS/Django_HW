"""
URL configuration for settings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# from currency.views import hello_world, rate_list, contact_us
import currency.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact_us/', views.contact_us),
    path('hello-world/', views.hello_world),
    path('template/', views.test_template),
    path('rate_list/', views.rate_list),
    path('source_list/', views.source_list),
    path('rate/update/<int:pk>/', views.rate_update),
    path('rate/delete/<int:pk>/', views.rate_delete),
    path('rate/details/<int:pk>/', views.rate_details),
    path('rate/create/', views.rate_create),
    path('source/create/', views.source_create),
    path('source/update/<int:pk>/', views.source_update),
    path('source/delete/<int:pk>/', views.source_delete),
    path('source/details/<int:pk>/', views.source_details),

]
