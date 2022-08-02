from django.contrib import admin
from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    path('login/', views.index, name="CRM Login Page"),
    path('register/', views.register, name="CRM Register Page"),
    path('dashboard/', views.dashboard, name="CRM Dashboard"),
    path('', views.home, name="CRM Home Page"),
]
