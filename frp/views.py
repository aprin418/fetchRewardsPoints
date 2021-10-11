from django.shortcuts import render, redirect
from .models import Payer
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect, request, response
import requests


def index(request):
    return render(request, 'index.html')


class PayerCreate(CreateView):
    model = Payer
    fields = ['name', 'points']

    def form_valid(self, form):
        print(self.__dict__)
        self.object = form.save(commit=False)
        self.object.save()
        print(self.object)
        return HttpResponseRedirect('/payers')


def payers(request):
    payers = Payer.objects.all()
    return render(request, 'payers.html', {'payers': payers})


class PayerUpdate(UpdateView):
    model = Payer
    fields = ['points']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/payers/' + str(self.object.pk))
