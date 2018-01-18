# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from location.models import ClassRoom,Lab

def lab(request):
    l=Lab.objects.all()
    return render(request, 'lab_tt.html',{'l':l})
def classroom(request):
    c=ClassRoom.objects.all()
    return render(request, 'class_tt.html',{'c':c})
# Create your views here.
