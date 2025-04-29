from django.urls import path
from . import views

urlpatterns = [
    path('', views.kisi_listesi, name='kisi_listesi'),
]
