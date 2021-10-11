from django.shortcuts import render
from .models import Payer
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html')
