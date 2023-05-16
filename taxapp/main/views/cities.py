from django.shortcuts import render
from ..models import *


def cities(request):
    return render(request, 'main/cities.html', {'title': 'Города'})
