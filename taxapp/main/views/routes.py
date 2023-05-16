from django.shortcuts import render
from ..models import *


def routes(request):
    return render(request, 'main/routes.html', {'title': 'Маршруты'})
