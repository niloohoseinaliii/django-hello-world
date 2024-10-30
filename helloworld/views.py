import datetime

from django.shortcuts import render

from .models import Counter
from .forms import HelloWorldForm


def index(request):
    return render(request, 'helloworld/index.html')
