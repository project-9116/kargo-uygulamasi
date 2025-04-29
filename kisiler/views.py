from django.shortcuts import render
from .models import Kisi

def kisi_listesi(request):
    kisiler = Kisi.objects.all()
    return render(request, 'kisiler/list.html', {'kisiler': kisiler})
