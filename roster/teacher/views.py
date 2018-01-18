# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from teacher.models import Teacher, Subject, Department
from semclass.models import Sem, Sec
from timet.models import Teacher_final, Master_final, Room_final, Lab_final
from location.models import ClassRoom, Lab
from location.lab_filter import search,check,search1
from location.room_filter import search2

def yoyo(request, string1, id):
    teacher = Teacher.objects.filter(id=id,department_name__department_initials=string1)
    tf=Teacher_final.objects.filter(teacher_name=teacher).order_by('day_type')
    return render(request,'tt1.html',{'tf':tf})

def Lab1(request, string1, id):
    a=10
    if string1=='A':
       a=0
    elif string1=='B':
        a=1
    elif string1=='C':
        a=2
    elif string1=='D':
        a=3
    else:
        pass
    lab = Lab.objects.filter(id=id,block=a)
    lf=Lab_final.objects.filter(lab_no=lab).order_by('day_type')
    return render(request,'tt1.html',{'tf':lf})
def Room1(request, string1, id):
    a=10
    if string1=='A':
       a=0
    elif string1=='B':
        a=1
    elif string1=='C':
        a=2
    elif string1=='D':
        a=3
    else:
        pass
    room = ClassRoom.objects.filter(id=id,block=a)
    rf=Room_final.objects.filter(lab_no=room).order_by('day_type')
    return render(request,'tt1.html',{'tf':rf})

def master_tt(request, string2, id, string4):
    sec=Sec.objects.filter(Section=string4,sem__sem=id,sem__department__department_initials=string2)
    mf=Master_final.objects.filter(sec=sec)
    return render(request, 'tt1.html',{'tf':mf})

def teacher1(request):
    teacher=Teacher.objects.all()
    department = Department.objects.all()
    return render(request, 'teacher_tt.html',{'t':teacher,'d':department})


def home(request):
    l = Lab.objects.all()
    for i in l:
        lf = Lab_final.objects.filter(lab_no=i)
        if lf.__len__() == 0:
            for j in range(0,6):
                l = Lab_final(lab_no=i, day_type=j + 1)
                l.save()
    c = ClassRoom.objects.all()
    for i in c:
        lf = Room_final.objects.filter(Room_no=i)
        if lf.__len__() == 0:
            for j in range(0, 6):
                l = Room_final(Room_no=i, day_type=j + 1)
                l.save()
    t = Teacher.objects.all()
    for i in t:
        lf = Teacher_final.objects.filter(teacher_name=i)
        if lf.__len__() == 0:
            for j in range(0, 6):
                l = Teacher_final(teacher_name=i, day_type=j + 1)
                l.save()
    m = Sec.objects.all().order_by('Section', 'sem')
    for i in m:
        lf = Master_final.objects.filter(sec=i)
        if lf.__len__() == 0:
            for j in range(0, 6):
                l = Master_final(sec=i, day_type=j + 1)
                l.save()
    sem = Sem.objects.all()
    li=list()
    s=''
    for i in sem:
        a=list()
        b=list()
        s= str(i.sem) + str(i.department.department_initials)
        sub = Subject.objects.filter(subject_code__startswith=s).filter(type_subject=1).order_by('-teaching_hours_a_day')
        tec = Teacher.objects.filter(department_name=i.department).order_by('teacher_name')
        for j in tec:
            for k in sub:
                if j.subject1 == k and j.teaching_hours_a_day_subject1 > 0:
                    if check(j,j.subject1,j.subject1.teaching_hours_a_day):
                        if j.subject1.teaching_hours_a_day == 3:
                            a.append([j, j.subject1, 1])
                        else:
                            b.append([j, j.subject1, 1])
                    else:
                        pass
                elif j.subject2 == k and j.teaching_hours_a_day_subject3 > 0:
                    if check(j,j.subject2,j.subject2.teaching_hours_a_day):
                        if j.subject2.teaching_hours_a_day == 3:
                            a.append([j, j.subject2, 2])
                        else:
                            b.append([j, j.subject2, 2])
                    else:
                        pass
                elif j.subject3 == k and j.teaching_hours_a_day_subject3 > 0:
                    if check(j,j.subject3,j.subject3.teaching_hours_a_day):
                        if j.subject3.teaching_hours_a_day == 3:
                            a.append([j, j.subject3, 3])
                        else:
                            b.append([j, j.subject3, 3])
                    else:
                        pass
                elif j.subject4 ==k and j.teaching_hours_a_day_subject4 > 0:
                    if check(j,j.subject4,j.subject4.teaching_hours_a_day):
                        if j.subject1.teaching_hours_a_day == 3:
                            a.append([j, j.subject4, 4])
                        else:
                            b.append([j, j.subject4, 4])
                    else:
                        pass
                else:
                    pass
        sec = Sec.objects.filter(sem=i).order_by('Section')
        for j in sec:
            d = search(a, j)
            e = search1(b, j)
    s=''
    for i in sem:
        c=list()
        s= str(i.sem) + str(i.department.department_initials)
        sub = Subject.objects.filter(subject_code__startswith=s).filter(type_subject=0).order_by('-teaching_hours_a_day')
        tec = Teacher.objects.filter(department_name=i.department).order_by('teacher_name')
        for j in tec:
            for k in sub:
                if j.subject1 == k and j.teaching_hours_a_day_subject1 > 0:
                    if check(j,j.subject1,j.subject1.teaching_hours_a_day):
                        c.append([j, j.subject1, 1])
                    else:
                        pass
                elif j.subject2 == k and j.teaching_hours_a_day_subject2 > 0:
                    if check(j,j.subject2,j.subject2.teaching_hours_a_day):
                        c.append([j, j.subject2, 2])
                    else:
                        pass
                elif j.subject3 == k and j.teaching_hours_a_day_subject3 > 0:
                    if check(j,j.subject3,j.subject3.teaching_hours_a_day):
                        c.append([j, j.subject3, 3])
                    else:
                        pass
                elif j.subject4 ==k and j.teaching_hours_a_day_subject4 > 0:
                    if check(j,j.subject4,j.subject4.teaching_hours_a_day):
                        c.append([j, j.subject4, 4])
                    else:
                        pass
                else:
                    pass
        sec = Sec.objects.filter(sem=i).order_by('Section')
        for j in sec:
            d = search2(c,j)
            li.append(d)
    return render(request, 'index.html')