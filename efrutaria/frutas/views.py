# frutas/views.py
from django.shortcuts import render
from .models import Fruta

def index(request):
    frutas = Fruta.objects.all()
    return render(request, 'frutas/index.html', {'frutas': frutas})
