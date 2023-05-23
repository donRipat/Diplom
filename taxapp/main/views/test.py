from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import *


def test(request):
    dic = {
        'title': 'TEST',
    }
    return render(request, 'main/test.html', dic)
