from models import Lab
from timet.models import Lab_final,Teacher_final,Master_final
from teacher.models import Subject,Teacher
def search(teacher,section):
    sub=list()
    lab=list()
    az=1
    lb = Lab.objects.all()
    mf = Master_final.objects.filter(sec=section).order_by('day_type')
    for i in teacher:
        az+=1
        z = i[0]
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
        if i[1] not in sub:
            sub.append(i[1])
        else:
            continue
        abc=0
        tf = Teacher_final.objects.filter(teacher_name=i[0]).order_by('day_type')
        for j in lb:
            if j in lab:
                continue
            lf = Lab_final.objects.filter(lab_no=j).order_by('day_type')

                                                             #part1

            if lf[0].p1 == lf[0].p2 == lf[0].p3 == lf[1].p1 == lf[1].p2 == lf[1].p3 == lf[2].p1 == lf[2].p2 == lf[2].p3 == '' and tf[0].p1 == tf[0].p2 == tf[0].p3 == tf[1].p1 == tf[1].p2 == tf[1].p3 == tf[2].p1 == tf[2].p2 == tf[2].p3 == '' and check_master(mf[0], mf[1],mf[2],i[1].teaching_hours_a_day,1.1) and lab_section(lf[0],lf[1],lf[2],section.Section) and abc==0:
                if ((tf[0].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[1].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[2].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day):
                    abc=1
                    break
                unique = str(str(section.sem.sem) + "," + str(section.sem.department.department_initials) + "," + str(section.Section) + "," + str(i[1].subject_initials))
                az+=1
                a = tf[0]
                b = tf[1]
                c = tf[2]
                d = lf[0]
                e = lf[1]
                f = lf[2]
                g = mf[0]
                h = mf[1]
                hh = mf[2]
                g.status = h.status = hh.status = 1
                d.sec = e.sec = f.sec = str(section.Section)
                unique += str(',' + str(j.lab_no))
                a.p1 = a.p2 = a.p3 = b.p1 = b.p2 = b.p3 = c.p1 = c.p2 = c.p3 = unique
                unique += str(',' + str(a.teacher_name.teacher_initials))
                d.p1 = d.p2 = d.p3 = e.p1 = e.p2 = e.p3 = f.p1 = f.p2 = f.p3 = unique
                if str(g.p1)=='':
                    s = str(g.p1)
                else:
                    s = ',' + str(g.p1)
                unique += str(s)
                g.p1 = g.p2 = g.p3 = h.p1 = h.p2 = h.p3 = hh.p1 = hh.p2 = hh.p3 = unique
                z = i[0]
                if i[2] == 1:
                    z.teaching_hours_a_day_subject1 -= i[1].teaching_hours_a_day
                elif i[2] == 2:
                    z.teaching_hours_a_day_subject2 -= i[1].teaching_hours_a_day
                elif i[2] == 3:
                    z.teaching_hours_a_day_subject3 -= i[1].teaching_hours_a_day
                elif i[2] == 4:
                    z.teaching_hours_a_day_subject4 -= i[1].teaching_hours_a_day
                a.teaching_hours += i[1].teaching_hours_a_day
                b.teaching_hours += i[1].teaching_hours_a_day
                c.teaching_hours += i[1].teaching_hours_a_day
                z.save()
                a.save()
                b.save()
                c.save()
                d.save()
                e.save()
                f.save()
                g.save()
                h.save()
                hh.save()
                lab.append(j)
                break

                                                    #PART 4

            elif lf[3].p4==lf[3].p5==lf[3].p6==lf[4].p4==lf[4].p5==lf[4].p6==lf[5].p4==lf[5].p5==lf[5].p6=='' and tf[3].p4==tf[3].p5==tf[3].p6==tf[4].p4==tf[4].p5==tf[4].p6==tf[5].p4==tf[5].p5==tf[5].p6==''and check_master(mf[3],mf[4],mf[5],i[1].teaching_hours_a_day,2.2) and lab_section(lf[3],lf[4],lf[5],section.Section) and abc==0:
                if ((tf[3].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[4].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[5].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day):
                    abc=1
                    break
                unique = str(str(section.sem.sem) + "," + str(section.sem.department.department_initials) + "," + str(section.Section) + "," + str(i[1].subject_initials))
                a = tf[3]
                b = tf[4]
                c = tf[5]
                d = lf[3]
                e = lf[4]
                f = lf[5]
                g = mf[3]
                h = mf[4]
                hh = mf[5]
                g.status = h.status = hh.status = 1
                d.sec = e.sec = f.sec = str(section.Section)
                unique += str(',' + str(j.lab_no))
                a.p4 = a.p5 = a.p6 = b.p4 = b.p5 = b.p6 = c.p4 = c.p5 = c.p6 = unique
                unique += str(',' + str(a.teacher_name.teacher_initials))
                d.p4 = d.p5 = d.p6 = e.p4 = e.p5 = e.p6 = f.p4 = f.p5 = f.p6 = unique
                if str(g.p4)=='':
                    s = str(g.p4)
                else:
                    s = ',' + str(g.p4)
                unique += str(s)
                g.p4 = g.p5 = g.p6 = h.p4 = h.p5 = h.p6 = hh.p4 = hh.p5 = hh.p6 = unique
                z = i[0]
                if i[2] == 1:
                    z.teaching_hours_a_day_subject1 -= i[1].teaching_hours_a_day
                elif i[2] == 2:
                    z.teaching_hours_a_day_subject2 -= i[1].teaching_hours_a_day
                elif i[2] == 3:
                    z.teaching_hours_a_day_subject3 -= i[1].teaching_hours_a_day
                elif i[2] == 4:
                    z.teaching_hours_a_day_subject4 -= i[1].teaching_hours_a_day
                a.teaching_hours += i[1].teaching_hours_a_day
                b.teaching_hours += i[1].teaching_hours_a_day
                c.teaching_hours += i[1].teaching_hours_a_day
                z.save()
                a.save()
                b.save()
                c.save()
                d.save()
                e.save()
                f.save()
                g.save()
                h.save()
                hh.save()
                lab.append(j)
                break

                                                        #PART 3

            elif lf[3].p1 == lf[3].p2 == lf[3].p3 == lf[4].p1 == lf[4].p2 == lf[4].p3 == lf[5].p1 == lf[5].p2 == lf[5].p3 == '' and tf[3].p1 == tf[3].p2 == tf[3].p3 == tf[4].p1 == tf[4].p2 == tf[4].p3 == tf[5].p1 == tf[5].p2 == tf[5].p3 == '' and check_master(mf[3],mf[4],mf[5],i[1].teaching_hours_a_day,2.1) and lab_section(lf[3],lf[4],lf[5],section.Section)and abc == 0:
                if ((tf[3].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[4].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[5].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day):
                    abc=1
                    break
                unique = str(str(section.sem.sem) + "," + str(section.sem.department.department_initials) + "," + str(section.Section) + "," + str(i[1].subject_initials))
                a = tf[3]
                b = tf[4]
                c = tf[5]
                d = lf[3]
                e = lf[4]
                f = lf[5]
                g = mf[3]
                h = mf[4]
                hh = mf[5]
                g.status = h.status = hh.status = 1
                d.sec = e.sec = f.sec = str(section.Section)
                unique += str(',' + str(j.lab_no))
                a.p1 = a.p2 = a.p3 = b.p1 = b.p2 = b.p3 = c.p1 = c.p2 = c.p3 = unique
                unique += str(',' + str(a.teacher_name.teacher_initials))
                d.p1 = d.p2 = d.p3 = e.p1 = e.p2 = e.p3 = f.p1 = f.p2 = f.p3 = unique
                if str(g.p1)=='':
                    s = str(g.p1)
                else:
                    s = ',' + str(g.p1)
                unique += str("," + s)
                g.p1 = g.p2 = g.p3 = h.p1 = h.p2 = h.p3 = hh.p1 = hh.p2 = hh.p3 = unique
                z = i[0]
                if i[2] == 1:
                    z.teaching_hours_a_day_subject1 -= i[1].teaching_hours_a_day
                elif i[2] == 2:
                    z.teaching_hours_a_day_subject2 -= i[1].teaching_hours_a_day
                elif i[2] == 3:
                    z.teaching_hours_a_day_subject3 -= i[1].teaching_hours_a_day
                elif i[2] == 4:
                    z.teaching_hours_a_day_subject4 -= i[1].teaching_hours_a_day
                a.teaching_hours += i[1].teaching_hours_a_day
                b.teaching_hours += i[1].teaching_hours_a_day
                c.teaching_hours += i[1].teaching_hours_a_day
                z.save()
                a.save()
                b.save()
                c.save()
                d.save()
                e.save()
                f.save()
                g.save()
                h.save()
                hh.save()
                lab.append(j)
                break

                                                #PART 2

            elif lf[0].p4 == lf[0].p5 == lf[0].p6 == lf[1].p4 == lf[1].p5 == lf[1].p6 == lf[2].p4 == lf[2].p5 == lf[2].p6 == '' and tf[0].p4 == tf[0].p5 == tf[0].p6 == tf[1].p4 == tf[1].p5 == tf[1].p6 == tf[2].p4 == tf[2].p5 == tf[2].p6 == '' and check_master(mf[0], mf[1],mf[2],i[1].teaching_hours_a_day,1.2) and lab_section(lf[0],lf[1],lf[2],section.Section) and abc==0:
                if ((tf[0].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[1].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[2].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day):
                    abc=1
                    break
                unique = str(str(section.sem.sem) + "," + str(section.sem.department.department_initials) + "," + str(section.Section) + "," + str(i[1].subject_initials))
                a = tf[0]
                b = tf[1]
                c = tf[2]
                d = lf[0]
                e = lf[1]
                f = lf[2]
                g = mf[0]
                h = mf[1]
                hh = mf[2]
                g.status = h.status = hh.status = 1
                d.sec = e.sec = f.sec = str(section.Section)
                unique += str(',' + str(j.lab_no))
                a.p4 = a.p5 = a.p6 = b.p4 = b.p5 = b.p6 = c.p4 = c.p5 = c.p6 = unique
                unique += str(',' + str(a.teacher_name.teacher_initials))
                d.p4 = d.p5 = d.p6 = e.p4 = e.p5 = e.p6 = f.p4 = f.p5 = f.p6 = unique
                if str(g.p4)=='':
                    s = str(g.p4)
                else:
                    s = ',' + str(g.p4)
                unique += str(s)
                g.p4 = g.p5 = g.p6 = h.p4 = h.p5 = h.p6 = hh.p4 = hh.p5 = hh.p6 = unique
                z = i[0]
                if i[2] == 1:
                    z.teaching_hours_a_day_subject1 -= i[1].teaching_hours_a_day
                elif i[2] == 2:
                    z.teaching_hours_a_day_subject2 -= i[1].teaching_hours_a_day
                elif i[2] == 3:
                    z.teaching_hours_a_day_subject3 -= i[1].teaching_hours_a_day
                elif i[2] == 4:
                    z.teaching_hours_a_day_subject4 -= i[1].teaching_hours_a_day
                a.teaching_hours += i[1].teaching_hours_a_day
                b.teaching_hours += i[1].teaching_hours_a_day
                c.teaching_hours += i[1].teaching_hours_a_day
                z.save()
                a.save()
                b.save()
                c.save()
                d.save()
                e.save()
                f.save()
                g.save()
                h.save()
                hh.save()
                lab.append(j)
                break

        if abc==1:
            continue
    return az

def search1(teacher,section):
    sub = list()
    lab = list()
    lb = Lab.objects.all()
    mf = Master_final.objects.filter(sec=section).order_by('day_type')
    for i in teacher:
        z = i[0]
        if i[2] == 1:
            if z.subject1 == i[1] and z.teaching_hours_a_day_subject1<=0:
                continue
        elif i[2] == 2:
            if z.subject2 == i[1] and z.teaching_hours_a_day_subject2<=0:
                continue
        elif i[2] == 3:
            if z.subject3 == i[1] and z.teaching_hours_a_day_subject3<=0:
                continue
        elif i[2] == 4:
            if z.subject4 == i[1] and z.teaching_hours_a_day_subject4<=0:
                continue
        abc=0
        tf = Teacher_final.objects.filter(teacher_name=i[0]).order_by('day_type')
        if i[1] not in sub:
            sub.append(i[1])
        else:
            continue
        for j in lb:
            if j in lab:
                continue
            lf = Lab_final.objects.filter(lab_no=j).order_by('day_type')
            if lf[3].p4 == lf[3].p5 == lf[4].p4 == lf[4].p5 == lf[5].p4 == lf[5].p5 == '' and tf[3].p4 == tf[3].p5 == tf[4].p4 == tf[4].p5 == tf[5].p4 == tf[5].p5 == '' and check_master1(mf[3], mf[4], mf[5],i[1].teaching_hours_a_day,2.3) and lab_section(lf[3],lf[4],lf[5],section.Section) and abc==0:
                if ((tf[3].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[4].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[5].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day):
                    abc=1
                    break
                unique = str(str(section.sem.sem) + "," + str(section.sem.department.department_initials) + "," + str(section.Section) + "," + str(i[1].subject_initials))
                a = tf[3]
                b = tf[4]
                c = tf[5]
                d = lf[3]
                e = lf[4]
                f = lf[5]
                g = mf[3]
                h = mf[4]
                hh = mf[5]
                g.status = h.status = hh.status = 1
                d.sec = e.sec = f.sec = str(section.Section)
                unique += str(',' + str(j.lab_no))
                a.p4 = a.p5 = b.p4 = b.p5 = c.p4 = c.p5 = unique
                unique += str(',' + str(a.teacher_name.teacher_initials))
                d.p4 = d.p5 = e.p4 = e.p5 = f.p4 = f.p5 = unique
                if str(g.p4)=='':
                    s = str(g.p4)
                else:
                    s = ',' + str(g.p4)
                unique += str(s)
                g.p4 = g.p5 = h.p4 = h.p5 = hh.p4 = hh.p5 = unique
                z = i[0]
                if i[2] == 1:
                    z.teaching_hours_a_day_subject1 -= i[1].teaching_hours_a_day
                elif i[2] == 2:
                    z.teaching_hours_a_day_subject2 -= i[1].teaching_hours_a_day
                elif i[2] == 3:
                    z.teaching_hours_a_day_subject3 -= i[1].teaching_hours_a_day
                elif i[2] == 4:
                    z.teaching_hours_a_day_subject4 -= i[1].teaching_hours_a_day
                a.teaching_hours += i[1].teaching_hours_a_day
                b.teaching_hours += i[1].teaching_hours_a_day
                c.teaching_hours += i[1].teaching_hours_a_day
                z.save()
                a.save()
                b.save()
                c.save()
                d.save()
                e.save()
                f.save()
                g.save()
                h.save()
                hh.save()
                lab.append(j)
                break
            elif lf[3].p5==lf[3].p6==lf[4].p5==lf[4].p6==lf[5].p5==lf[5].p6=='' and tf[3].p5==tf[3].p6==tf[4].p5==tf[4].p6==tf[5].p5==tf[5].p6==''and check_master1(mf[3],mf[4],mf[5],i[1].teaching_hours_a_day,2.4) and lab_section(lf[3],lf[4],lf[5],section.Section) and abc==0:
                if ((tf[3].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[4].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[5].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day):
                    abc=1
                    break
                unique = str(str(section.sem.sem) + "," + str(section.sem.department.department_initials) + "," + str(section.Section) + "," + str(i[1].subject_initials))
                a = tf[3]
                b = tf[4]
                c = tf[5]
                d = lf[3]
                e = lf[4]
                f = lf[5]
                g = mf[3]
                h = mf[4]
                hh = mf[5]
                g.status = h.status = hh.status = 1
                d.sec = e.sec = f.sec = str(section.Section)
                unique += str(',' + str(j.lab_no))
                a.p5 = a.p6 = b.p5 = b.p6 = c.p5 = c.p6 = unique
                unique += str(',' + str(a.teacher_name.teacher_initials))
                d.p5 = d.p6 = e.p5 = e.p6 = f.p5 = f.p6 = unique
                if str(g.p5)=='':
                    s = str(g.p5)
                else:
                    s = ',' + str(g.p5)
                unique += str(s)
                g.p5 = g.p6 = h.p5 = h.p6 = hh.p5 = hh.p6 = unique
                z = i[0]
                if i[2] == 1:
                    z.teaching_hours_a_day_subject1 -= i[1].teaching_hours_a_day
                elif i[2] == 2:
                    z.teaching_hours_a_day_subject2 -= i[1].teaching_hours_a_day
                elif i[2] == 3:
                    z.teaching_hours_a_day_subject3 -= i[1].teaching_hours_a_day
                elif i[2] == 4:
                    z.teaching_hours_a_day_subject4 -= i[1].teaching_hours_a_day
                a.teaching_hours += i[1].teaching_hours_a_day
                b.teaching_hours += i[1].teaching_hours_a_day
                c.teaching_hours += i[1].teaching_hours_a_day
                z.save()
                a.save()
                b.save()
                c.save()
                d.save()
                e.save()
                f.save()
                g.save()
                h.save()
                hh.save()
                lab.append(j)
                break
            elif lf[0].p1 == lf[0].p2 == lf[1].p1 == lf[1].p2 == lf[2].p1 == lf[2].p2 == '' and tf[0].p1 == tf[0].p2 == tf[1].p1 == tf[1].p2 == tf[2].p1 == tf[2].p2 == '' and check_master1(mf[0], mf[1],mf[2],i[1].teaching_hours_a_day,1.1) and lab_section(lf[0],lf[1],lf[2],section.Section) and abc==0:
                if ((tf[0].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[1].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[2].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day):
                    abc=1
                    break
                unique = str(str(section.sem.sem) + "," + str(section.sem.department.department_initials) + "," + str(section.Section) + "," + str(i[1].subject_initials))
                a = tf[0]
                b = tf[1]
                c = tf[2]
                d = lf[0]
                e = lf[1]
                f = lf[2]
                g = mf[0]
                h = mf[1]
                hh = mf[2]
                g.status = h.status = hh.status = 1
                d.sec = e.sec = f.sec = str(section.Section)
                unique += str(',' + str(j.lab_no))
                a.p1 = a.p2 = b.p1 = b.p2 = c.p1 = c.p2 = unique
                unique += str(',' + str(a.teacher_name.teacher_initials))
                d.p1 = d.p2 = e.p1 = e.p2 = f.p1 = f.p2 = unique
                if str(g.p1)=='':
                    s = str(g.p1)
                else:
                    s = ',' + str(g.p1)
                unique += str(s)
                g.p1 = g.p2 = h.p1 = h.p2 = hh.p1 = hh.p2 = unique
                z = i[0]
                if i[2] == 1:
                    z.teaching_hours_a_day_subject1 -= i[1].teaching_hours_a_day
                elif i[2] == 2:
                    z.teaching_hours_a_day_subject2 -= i[1].teaching_hours_a_day
                elif i[2] == 3:
                    z.teaching_hours_a_day_subject3 -= i[1].teaching_hours_a_day
                elif i[2] == 4:
                    z.teaching_hours_a_day_subject4 -= i[1].teaching_hours_a_day
                a.teaching_hours += i[1].teaching_hours_a_day
                b.teaching_hours += i[1].teaching_hours_a_day
                c.teaching_hours += i[1].teaching_hours_a_day
                z.save()
                a.save()
                b.save()
                c.save()
                d.save()
                e.save()
                f.save()
                g.save()
                h.save()
                hh.save()
                lab.append(j)
                break
            elif lf[0].p2 == lf[0].p3 == lf[1].p2 == lf[1].p3 == lf[2].p2 == lf[2].p3 == '' and tf[0].p2 == tf[0].p3 == tf[1].p2 == tf[1].p3 == tf[2].p2 == tf[2].p3 == '' and check_master1(mf[0],mf[1],mf[2],i[1].teaching_hours_a_day,1.2) and lab_section(lf[0],lf[1],lf[2],section.Section) and abc==0:
                if ((tf[0].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[1].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[2].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day):
                    abc=1
                    break
                unique = str(str(section.sem.sem) + "," + str(section.sem.department.department_initials) + "," + str(section.Section) + "," + str(i[1].subject_initials))
                a = tf[0]
                b = tf[1]
                c = tf[2]
                d = lf[0]
                e = lf[1]
                f = lf[2]
                g = mf[0]
                h = mf[1]
                hh = mf[2]
                g.status = h.status = hh.status = 1
                d.sec = e.sec = f.sec = str(section.Section)
                unique += str(',' + str(j.lab_no))
                a.p2 = a.p3 = b.p2 = b.p3 = c.p2 = c.p3 = unique
                unique += str(',' + str(a.teacher_name.teacher_initials))
                d.p2 = d.p3 = e.p2 = e.p3 = f.p2 = f.p3 = unique
                if str(g.p2)=='':
                    s = str(g.p2)
                else:
                    s = ',' + str(g.p2)
                unique += str("," + s)
                g.p2 = g.p3  = h.p2 = h.p3 = hh.p2 = hh.p3 = unique
                if i[2] == 1:
                    z.teaching_hours_a_day_subject1 -= i[1].teaching_hours_a_day
                elif i[2] == 2:
                    z.teaching_hours_a_day_subject2 -= i[1].teaching_hours_a_day
                elif i[2] == 3:
                    z.teaching_hours_a_day_subject3 -= i[1].teaching_hours_a_day
                elif i[2] == 4:
                    z.teaching_hours_a_day_subject4 -= i[1].teaching_hours_a_day
                a.teaching_hours += i[1].teaching_hours_a_day
                b.teaching_hours += i[1].teaching_hours_a_day
                c.teaching_hours += i[1].teaching_hours_a_day
                z.save()
                a.save()
                b.save()
                c.save()
                d.save()
                e.save()
                f.save()
                g.save()
                h.save()
                hh.save()
                lab.append(j)
                break
            elif lf[3].p1 == lf[3].p2 == lf[4].p1 == lf[4].p2 == lf[5].p1 == lf[5].p2 == '' and tf[3].p1 == tf[3].p2 == tf[4].p1 == tf[4].p2 == tf[5].p1 == tf[5].p2 == '' and check_master1(mf[3], mf[4], mf[5],i[1].teaching_hours_a_day,2.1) and lab_section(lf[3],lf[4],lf[5],section.Section) and abc==0:
                if ((tf[3].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[4].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[5].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day):
                    abc=1
                    break
                unique = str(str(section.sem.sem) + "," + str(section.sem.department.department_initials) + "," + str(section.Section) + "," + str(i[1].subject_initials))
                a = tf[3]
                b = tf[4]
                c = tf[5]
                d = lf[3]
                e = lf[4]
                f = lf[5]
                g = mf[3]
                h = mf[4]
                hh = mf[5]
                g.status = h.status = hh.status = 1
                d.sec = e.sec = f.sec = str(section.Section)
                unique += str(',' + str(j.lab_no))
                a.p1 = a.p2 = b.p1 = b.p2 = c.p1 = c.p2 = unique
                unique += str(',' + str(a.teacher_name.teacher_initials))
                d.p1 = d.p2 = e.p1 = e.p2 = f.p1 = f.p2 = unique
                if str(g.p1)=='':
                    s = str(g.p1)
                else:
                    s = ',' + str(g.p1)
                unique += str(s)
                g.p1 = g.p2 = h.p1 = h.p2 = hh.p1 = hh.p2 = unique
                z = i[0]
                if i[2] == 1:
                    z.teaching_hours_a_day_subject1 -= i[1].teaching_hours_a_day
                elif i[2] == 2:
                    z.teaching_hours_a_day_subject2 -= i[1].teaching_hours_a_day
                elif i[2] == 3:
                    z.teaching_hours_a_day_subject3 -= i[1].teaching_hours_a_day
                elif i[2] == 4:
                    z.teaching_hours_a_day_subject4 -= i[1].teaching_hours_a_day
                a.teaching_hours += i[1].teaching_hours_a_day
                b.teaching_hours += i[1].teaching_hours_a_day
                c.teaching_hours += i[1].teaching_hours_a_day
                z.save()
                a.save()
                b.save()
                c.save()
                d.save()
                e.save()
                f.save()
                g.save()
                h.save()
                hh.save()
                lab.append(j)
                break
            elif lf[3].p2 == lf[3].p3 == lf[4].p2 == lf[4].p3 == lf[5].p2 == lf[5].p3 == '' and tf[3].p2 == tf[3].p3 == tf[4].p2 == tf[4].p3 == tf[5].p2 == tf[5].p3 == '' and check_master1(mf[3],mf[4],mf[5],i[1].teaching_hours_a_day,2.2) and lab_section(lf[3],lf[4],lf[5],section.Section) and abc==0:
                if ((tf[3].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[4].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[5].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day):
                    abc=1
                    break
                unique = str(str(section.sem.sem) + "," + str(section.sem.department.department_initials) + "," + str(section.Section) + "," + str(i[1].subject_initials))
                a = tf[3]
                b = tf[4]
                c = tf[5]
                d = lf[3]
                e = lf[4]
                f = lf[5]
                g = mf[3]
                h = mf[4]
                hh = mf[5]
                g.status = h.status = hh.status = 1
                d.sec = e.sec = f.sec = str(section.Section)
                unique += str(',' + str(j.lab_no))
                a.p2 = a.p3 = b.p2 = b.p3 = c.p2 = c.p3 = unique
                unique += str(',' + str(a.teacher_name.teacher_initials))
                d.p2 = d.p3 = e.p2 = e.p3 = f.p2 = f.p3 = unique
                if str(g.p2)=='':
                    s = str(g.p2)
                else:
                    s = ',' + str(g.p2)
                unique += str("," + s)
                g.p2 = g.p3  = h.p2 = h.p3 = hh.p2 = hh.p3 = unique
                if i[2] == 1:
                    z.teaching_hours_a_day_subject1 -= i[1].teaching_hours_a_day
                elif i[2] == 2:
                    z.teaching_hours_a_day_subject2 -= i[1].teaching_hours_a_day
                elif i[2] == 3:
                    z.teaching_hours_a_day_subject3 -= i[1].teaching_hours_a_day
                elif i[2] == 4:
                    z.teaching_hours_a_day_subject4 -= i[1].teaching_hours_a_day
                a.teaching_hours += i[1].teaching_hours_a_day
                b.teaching_hours += i[1].teaching_hours_a_day
                c.teaching_hours += i[1].teaching_hours_a_day
                z.save()
                a.save()
                b.save()
                c.save()
                d.save()
                e.save()
                f.save()
                g.save()
                h.save()
                hh.save()
                lab.append(j)
                break
            elif lf[0].p4 == lf[0].p5 == lf[1].p4 == lf[1].p5 == lf[2].p4 == lf[2].p5 == '' and tf[0].p4 == tf[0].p5 == tf[1].p4 == tf[1].p5 == tf[2].p4 == tf[2].p5 == '' and check_master1(mf[0], mf[1],mf[2],i[1].teaching_hours_a_day,1.3) and lab_section(lf[0],lf[1],lf[2],section.Section) and abc==0:
                if ((tf[0].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[1].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[2].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day):
                    abc=1
                    break
                unique = str(str(section.sem.sem) + "," + str(section.sem.department.department_initials) + "," + str(section.Section) + "," + str(i[1].subject_initials))
                a = tf[0]
                b = tf[1]
                c = tf[2]
                d = lf[0]
                e = lf[1]
                f = lf[2]
                g = mf[0]
                h = mf[1]
                hh = mf[2]
                g.status = h.status = hh.status = 1
                d.sec = e.sec = f.sec = str(section.Section)
                unique += str(',' + str(j.lab_no))
                a.p4 = a.p5 = b.p4 = b.p5 = c.p4 = c.p5 = unique
                unique += str(',' + str(a.teacher_name.teacher_initials))
                d.p4 = d.p5 = e.p4 = e.p5 = f.p4 = f.p5 = unique
                if str(g.p4)=='':
                    s = str(g.p4)
                else:
                    s = ',' + str(g.p4)
                unique += str(s)
                g.p4 = g.p5 = h.p4 = h.p5 = hh.p4 = hh.p5 = unique
                z = i[0]
                if i[2] == 1:
                    z.teaching_hours_a_day_subject1 -= i[1].teaching_hours_a_day
                elif i[2] == 2:
                    z.teaching_hours_a_day_subject2 -= i[1].teaching_hours_a_day
                elif i[2] == 3:
                    z.teaching_hours_a_day_subject3 -= i[1].teaching_hours_a_day
                elif i[2] == 4:
                    z.teaching_hours_a_day_subject4 -= i[1].teaching_hours_a_day
                a.teaching_hours += i[1].teaching_hours_a_day
                b.teaching_hours += i[1].teaching_hours_a_day
                c.teaching_hours += i[1].teaching_hours_a_day
                z.save()
                a.save()
                b.save()
                c.save()
                d.save()
                e.save()
                f.save()
                g.save()
                h.save()
                hh.save()
                lab.append(j)
                break
            elif lf[0].p5==lf[0].p6==lf[1].p5==lf[1].p6==lf[2].p5==lf[2].p6=='' and tf[0].p5==tf[0].p6==tf[1].p5==tf[1].p6==tf[2].p5==tf[2].p6==''and check_master1(mf[0],mf[1],mf[2],i[1].teaching_hours_a_day,1.4) and lab_section(lf[0],lf[1],lf[2],section.Section) and abc==0:
                if ((tf[0].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[1].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day) or ((tf[2].teaching_hours + i[1].teaching_hours_a_day) > i[0].total_teaching_hours_a_day):
                    abc=1
                    break
                unique = str(str(section.sem.sem) + "," + str(section.sem.department.department_initials) + "," + str(section.Section) + "," + str(i[1].subject_initials))
                a = tf[0]
                b = tf[1]
                c = tf[2]
                d = lf[0]
                e = lf[1]
                f = lf[2]
                g = mf[0]
                h = mf[1]
                hh = mf[2]
                g.status = h.status = hh.status = 1
                d.sec = e.sec = f.sec = str(section.Section)
                unique += str(',' + str(j.lab_no))
                a.p5 = a.p6 = b.p5 = b.p6 = c.p5 = c.p6 = unique
                unique += str(',' + str(a.teacher_name.teacher_initials))
                d.p5 = d.p6 = e.p5 = e.p6 = f.p5 = f.p6 = unique
                if str(g.p5)=='':
                    s = str(g.p5)
                else:
                    s = ',' + str(g.p5)
                unique += str(s)
                g.p5 = g.p6 = h.p5 = h.p6 = hh.p5 = hh.p6 = unique
                z = i[0]
                if i[2] == 1:
                    z.teaching_hours_a_day_subject1 -= i[1].teaching_hours_a_day
                elif i[2] == 2:
                    z.teaching_hours_a_day_subject2 -= i[1].teaching_hours_a_day
                elif i[2] == 3:
                    z.teaching_hours_a_day_subject3 -= i[1].teaching_hours_a_day
                elif i[2] == 4:
                    z.teaching_hours_a_day_subject4 -= i[1].teaching_hours_a_day
                a.teaching_hours += i[1].teaching_hours_a_day
                b.teaching_hours += i[1].teaching_hours_a_day
                c.teaching_hours += i[1].teaching_hours_a_day
                z.save()
                a.save()
                b.save()
                c.save()
                d.save()
                e.save()
                f.save()
                g.save()
                h.save()
                hh.save()
                lab.append(j)
                break
        if abc==1:
            continue
    return teacher

def check_master1(m1,m2,m3,hours,code):
    if code == 1.1 or code == 2.1:
        if m1.status==1 and m2.status==1 and m3.status==1:
            if m1.p1 == m1.p2 == m2.p1 ==m2.p2 == m3.p1 == m3.p2 == '':
                return False
            elif m1.p1 == m1.p2 == m2.p1 ==m2.p2 == m3.p1 == m3.p2:
                l = m1.p1.split(',')
                if check_lab(l[3], hours):
                    return True
                else:
                    return False
            else:
                return False
        elif m1.status==0 and m2.status==0 and m3.status==0:
            if m1.p1 == m1.p2 == m2.p1 ==m2.p2 == m3.p1 == m3.p2 == '':
                return True
            else:
                return False
    elif code == 1.2 or code == 2.2:
        if m1.status==1 and m2.status==1 and m3.status==1:
            if m1.p2 == m1.p3 == m2.p2 ==m2.p3 == m3.p2 == m3.p3 == '':
                return False
            elif m1.p2 == m1.p3 == m2.p2 ==m2.p3 == m3.p2 == m3.p3:
                l = m1.p2.split(',')
                if check_lab(l[3], hours):
                    return True
                else:
                    return False
            else:
                return False
        elif m1.status==0 and m2.status==0 and m3.status==0:
            if m1.p2 == m1.p3 == m2.p2 ==m2.p3 == m3.p2 == m3.p3 == '':
                return True
            else:
                return False
    elif code == 1.3 or code == 2.3:
        if m1.status==1 and m2.status==1 and m3.status==1:
            if m1.p4 == m1.p5 == m2.p4 == m2.p5 == m3.p4 == m3.p5 == '':
                return False
            elif m1.p4 == m1.p5 == m2.p4 ==m2.p5 == m3.p4 == m3.p5:
                l = m1.p4.split(',')
                if check_lab(l[3], hours):
                    return True
                else:
                    return False
            else:
                return False
        elif m1.status==0 and m2.status==0 and m3.status==0:
            if m1.p4 == m1.p5 == m2.p4 ==m2.p5 == m3.p4 == m3.p5 == '':
                return True
            else:
                return False
    elif code == 1.4 or code == 2.4:
        if m1.status==1 and m2.status==1 and m3.status==1:
            if m1.p5 == m1.p6 == m2.p5 ==m2.p6 == m3.p5 == m3.p6 == '':
                return False
            elif m1.p5 == m1.p6 == m2.p5 ==m2.p6 == m3.p5 == m3.p6:
                l = m1.p5.split(',')
                if check_lab(l[3], hours):
                    return True
                else:
                    return False
            else:
                return False
        elif m1.status==0 and m2.status==0 and m3.status==0:
            if m1.p5 == m1.p6 == m2.p5 ==m2.p6 == m3.p5 == m3.p6 == '':
                return True
            else:
                return False


def check_master(m1, m2, m3, hours,code):
   if code==1.1 or code==2.1:
       if m1.status==1 and m2.status==1 and m3.status==1:
           if m1.p1 == m1.p2 == m1.p3 == m2.p1 == m2.p2 == m2.p3 == m3.p1 == m3.p2 == m3.p3 == '':
               return False
           elif m1.p1 == m1.p2 == m1.p2 == m2.p1 == m2.p2 == m2.p3 == m3.p1 == m3.p2 == m3.p3:
               l = m1.p1.split(',')
               if check_lab(l[3],hours):
                   return True
               else:
                   return False
           else:
               return False
       elif m1.status==0 and m2.status==0 and m3.status==0:
           if m1.p1 == m1.p2 == m1.p2 == m2.p1 == m2.p2 == m2.p3 == m3.p1 == m3.p2 == m3.p3 == '':
               return True
           else:
               return False
   elif code==1.2 or code == 2.2:
       if m1.status==1 and m2.status==1 and m3.status==1:
           if m1.p4 == m1.p5 == m1.p6 == m2.p4 == m2.p5 == m2.p6 == m3.p4 == m3.p5 == m3.p6 == '':
               return False
           elif m1.p4 == m1.p5 == m1.p6 == m2.p4 == m2.p5 == m2.p6 == m3.p4 == m3.p5 == m3.p6:
               l=m1.p4.split(',')
               if check_lab(l[3],hours):
                   return True
               else:
                   return False
           else:
               return False
       elif m1.status==0 and m2.status==0 and m3.status==0:
           if m1.p4 == m1.p5 == m1.p6 == m2.p4 == m2.p5 == m2.p6 == m3.p4 == m3.p5 == m3.p6 == '':
               return True
           else:
               return False
   else:
       return False

def check_lab(sub_initials,hours):
    sub=Subject.objects.get(subject_initials=sub_initials)
    if sub.teaching_hours_a_day == hours:
        return True
    else:
        return False
def lab_section(l1,l2,l3,section):
    if l1.sec==l2.sec==l3.sec=='':
        l1.sec=l2.sec=l3.sec=section
        l1.save()
        l2.save()
        l3.save()
        return True
    else:
        if l1.sec==l2.sec==l3.sec:
            if l1.sec==section:
                return False
            else:
                return True
        else:
            return False

                        ## To cheak the availability of teacher according to the teaching hours

def check(teacher,subject,hours):
    a=subject.teaching_hours_per_week
    t = Teacher_final.objects.filter(teacher_name=teacher).order_by('day_type')
    c = 0
    for i in t:
        if (i.teaching_hours+hours) <= teacher.total_teaching_hours_a_day:
            c += 1
    if c >= a:
        return True
    else:
        return False