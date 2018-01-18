from location.models import ClassRoom
from timet.models import Room_final, Master_final, Teacher_final

def search2(teacher,section):
    sub = list()
    li=list()
    n = 1
    cr = ClassRoom.objects.all()
    for j in cr:
        if j.sec1!=None and j.sec2!=None:
            continue
        else:
            pass
        for i in teacher:
            mf = Master_final.objects.filter(sec=section).order_by('day_type')
            rf = Room_final.objects.filter(Room_no=j).order_by('day_type')
            z = i[0]
            n=i[1].teaching_hours_per_week
            if i[1] in sub:
                continue
            else:
                pass
            if i[2] == 1:
                if z.subject1 == i[1] and z.teaching_hours_a_day_subject1 <= 0:
                    continue
            elif i[2] == 2:
                if z.subject2 == i[1] and z.teaching_hours_a_day_subject2 <= 0:
                    continue
            elif i[2] == 3:
                if z.subject3 == i[1] and z.teaching_hours_a_day_subject3 <= 0:
                    continue
            elif i[2] == 4:
                if z.subject4 == i[1] and z.teaching_hours_a_day_subject4 <= 0:
                    continue
            else:
                pass
            tf = Teacher_final.objects.filter(teacher_name=i[0]).order_by('day_type')
            x=0
            for k in range(0,7):
                if x==n:
                    li.append([i[0],i[1]])
                    sub.append(i[1])
                    break
                elif x!=n and k==6:
                    break
                else:
                    pass
                unique = str(str(section.sem.sem) + "," + str(section.sem.department.department_initials) + "," + str(section.Section) + "," + str(i[1].subject_initials))
                if mf[k].p1==tf[k].p1==rf[k].p1=='':
                    if ((tf[k].teaching_hours + i[1].teaching_hours_a_day) <= i[0].total_teaching_hours_a_day):
                        x+=1
                        li.append([x,1,n,i[0]])
                        a=tf[k]
                        b=rf[k]
                        c=mf[k]
                        b.p1 = unique
                        unique += str(',' + str(j.room_no))
                        a.p1 = unique
                        unique += str(',' + str(a.teacher_name.teacher_initials))
                        c.p1 = unique
                        a.teaching_hours += i[1].teaching_hours_a_day
                        a.save()
                        b.save()
                        c.save()
                        if i[2] == 1:
                            z.teaching_hours_a_day_subject1 -= i[1].teaching_hours_a_day
                        elif i[2] == 2:
                            z.teaching_hours_a_day_subject2 -= i[1].teaching_hours_a_day
                        elif i[2] == 3:
                            z.teaching_hours_a_day_subject3 -= i[1].teaching_hours_a_day
                        elif i[2] == 4:
                            z.teaching_hours_a_day_subject4 -= i[1].teaching_hours_a_day
                        z.save()
                elif mf[k].p2==tf[k].p2==rf[k].p2=='':
                    if ((tf[k].teaching_hours + i[1].teaching_hours_a_day) <= i[0].total_teaching_hours_a_day):
                        x+=1
                        li.append([x,2,n,i[0]])
                        a=tf[k]
                        b=rf[k]
                        c=mf[k]
                        b.p2 = unique
                        unique += str(',' + str(j.room_no))
                        a.p2 = unique
                        unique += str(',' + str(a.teacher_name.teacher_initials))
                        c.p2 = unique
                        a.teaching_hours += i[1].teaching_hours_a_day
                        a.save()
                        b.save()
                        c.save()
                        if i[2] == 1:
                            z.teaching_hours_a_day_subject1 -= i[1].teaching_hours_a_day
                        elif i[2] == 2:
                            z.teaching_hours_a_day_subject2 -= i[1].teaching_hours_a_day
                        elif i[2] == 3:
                            z.teaching_hours_a_day_subject3 -= i[1].teaching_hours_a_day
                        elif i[2] == 4:
                            z.teaching_hours_a_day_subject4 -= i[1].teaching_hours_a_day
                        z.save()
                elif mf[k].p3==tf[k].p3==rf[k].p3=='':
                    if ((tf[k].teaching_hours + i[1].teaching_hours_a_day) <= i[0].total_teaching_hours_a_day):
                        x+=1
                        li.append([x,3,n,i[0]])
                        a=tf[k]
                        b=rf[k]
                        c=mf[k]
                        b.p3 = unique
                        unique += str(',' + str(j.room_no))
                        a.p3 = unique
                        unique += str(',' + str(a.teacher_name.teacher_initials))
                        c.p3 = unique
                        a.teaching_hours += i[1].teaching_hours_a_day
                        a.save()
                        b.save()
                        c.save()
                        if i[2] == 1:
                            z.teaching_hours_a_day_subject1 -= i[1].teaching_hours_a_day
                        elif i[2] == 2:
                            z.teaching_hours_a_day_subject2 -= i[1].teaching_hours_a_day
                        elif i[2] == 3:
                            z.teaching_hours_a_day_subject3 -= i[1].teaching_hours_a_day
                        elif i[2] == 4:
                            z.teaching_hours_a_day_subject4 -= i[1].teaching_hours_a_day
                        z.save()
                elif mf[k].p4==tf[k].p4==rf[k].p4=='':
                    if ((tf[k].teaching_hours + i[1].teaching_hours_a_day) <= i[0].total_teaching_hours_a_day):
                        x+=1
                        li.append([x,4,n,i[0]])
                        a=tf[k]
                        b=rf[k]
                        c=mf[k]
                        b.p4 = unique
                        unique += str(',' + str(j.room_no))
                        a.p4 = unique
                        unique += str(',' + str(a.teacher_name.teacher_initials))
                        c.p4 = unique
                        a.teaching_hours += i[1].teaching_hours_a_day
                        a.save()
                        b.save()
                        c.save()
                        if i[2] == 1:
                            z.teaching_hours_a_day_subject1 -= i[1].teaching_hours_a_day
                        elif i[2] == 2:
                            z.teaching_hours_a_day_subject2 -= i[1].teaching_hours_a_day
                        elif i[2] == 3:
                            z.teaching_hours_a_day_subject3 -= i[1].teaching_hours_a_day
                        elif i[2] == 4:
                            z.teaching_hours_a_day_subject4 -= i[1].teaching_hours_a_day
                        z.save()
                elif mf[k].p5==tf[k].p5==rf[k].p5=='':
                    if ((tf[k].teaching_hours + i[1].teaching_hours_a_day) <= i[0].total_teaching_hours_a_day):
                        x+=1
                        li.append([x,5,n,i[0]])
                        a=tf[k]
                        b=rf[k]
                        c=mf[k]
                        b.p5 = unique
                        unique += str(',' + str(j.room_no))
                        a.p5 = unique
                        unique += str(',' + str(a.teacher_name.teacher_initials))
                        c.p5 = unique
                        a.teaching_hours += i[1].teaching_hours_a_day
                        a.save()
                        b.save()
                        c.save()
                        if i[2] == 1:
                            z.teaching_hours_a_day_subject1 -= i[1].teaching_hours_a_day
                        elif i[2] == 2:
                            z.teaching_hours_a_day_subject2 -= i[1].teaching_hours_a_day
                        elif i[2] == 3:
                            z.teaching_hours_a_day_subject3 -= i[1].teaching_hours_a_day
                        elif i[2] == 4:
                            z.teaching_hours_a_day_subject4 -= i[1].teaching_hours_a_day
                        z.save()
                elif mf[k].p6==tf[k].p6==rf[k].p6=='':
                    if ((tf[k].teaching_hours + i[1].teaching_hours_a_day) <= i[0].total_teaching_hours_a_day):
                        x+=1
                        li.append([x,6,n,i[0]])
                        a=tf[k]
                        b=rf[k]
                        c=mf[k]
                        b.p6 = unique
                        unique += str(',' + str(j.room_no))
                        a.p6 = unique
                        unique += str(',' + str(a.teacher_name.teacher_initials))
                        c.p6 = unique
                        a.teaching_hours += i[1].teaching_hours_a_day
                        a.save()
                        b.save()
                        c.save()
                        if i[2] == 1:
                            z.teaching_hours_a_day_subject1 -= i[1].teaching_hours_a_day
                        elif i[2] == 2:
                            z.teaching_hours_a_day_subject2 -= i[1].teaching_hours_a_day
                        elif i[2] == 3:
                            z.teaching_hours_a_day_subject3 -= i[1].teaching_hours_a_day
                        elif i[2] == 4:
                            z.teaching_hours_a_day_subject4 -= i[1].teaching_hours_a_day
                        z.save()
        if sub.__len__()==6:
            abc=j
            if abc.sec1==None:
                abc.sec1=section
            else:
                abc.sec2=section
            abc.save()
            break
    return [sub,li]
#5111551458