from django.shortcuts import render
from ..models import *


def clients(request):
    return render(request, 'main/clients.html', {'title': 'Клиенты'})
