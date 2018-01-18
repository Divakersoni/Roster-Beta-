# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from teacher.models import Department
from semclass.models import Sem, Sec
from django.shortcuts import render

def master(request):
    sem=Sem.objects.all()
    sec=Sec.objects.all()
    department=Department.objects.all()
    return render(request, 'master_tt.html', {'sem':sem, 'sec':sec, 'dep':department})

