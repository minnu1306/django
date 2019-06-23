# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Rem
from .forms import RemForm

def index(request):
    rem_list = Rem.objects.order_by('id')
    form = RemForm()
    context = {'rem_list' : rem_list, 'form' : form}
    return render(request, 'rem/index.html',context)
def addRem(request):
    form = RemForm(request.POST)
    if form.is_valid():
        new_rem = Rem(text=request.POST['text'], time=request.POST['time'])
        new_rem.save()
    return redirect('index')

def details(request, id):
    rem = Rem.objects.get(id=id)
    context = { 'rem':rem}
    return render (request, 'details.html',context)

def completeRem(request, id):
    rem = Rem.objects.get(id=id)
    rem.complete = True
    rem.save()
    return redirect('index')
