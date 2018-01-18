# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from teacher.models import Teacher
from location.models import ClassRoom
from location.models import Lab
from semclass.models import Sec
class Teacher_final(models.Model):
   day1 = 1
   day2 = 2
   day3 = 3
   day4 = 4
   day5 = 5
   day6 = 6
   Type_Day = (
       (day1, 'Monday'),
       (day2, 'Tuesday'),
       (day3, 'Wednesday'),
       (day4, 'Thrusday'),
       (day5, 'Friday'),
       (day6, 'Saturday'),
   )
   teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE)
   teaching_hours = models.SmallIntegerField(default=0)
   day_type = models.SmallIntegerField(choices=Type_Day, default=day1)
   p1 = models.CharField(max_length=1000, blank=True, null=True, default="")
   p2 = models.CharField(max_length=1000, blank=True, null=True, default="")
   p3 = models.CharField(max_length=1000, blank=True, null=True, default="")
   p4 = models.CharField(max_length=1000, blank=True, null=True, default="")
   p5 = models.CharField(max_length=1000, blank=True, null=True, default="")
   p6 = models.CharField(max_length=1000, blank=True, null=True, default="")
   def __str__(self):
      return self.teacher_name.teacher_name

class Room_final(models.Model):
   day1 = 1
   day2 = 2
   day3 = 3
   day4 = 4
   day5 = 5
   day6 = 6
   Type_Day = (
       (day1, 'Monday'),
       (day2, 'Tuesday'),
       (day3, 'Wednesday'),
       (day4, 'Thrusday'),
       (day5, 'Friday'),
       (day6, 'Saturday'),
   )
   Room_no = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
   day_type = models.SmallIntegerField(choices=Type_Day, default=day1)
   p1 = models.CharField(max_length=100, blank=True, null=True, default="")
   p2 = models.CharField(max_length=100, blank=True, null=True, default="")
   p3 = models.CharField(max_length=100, blank=True, null=True, default="")
   p4 = models.CharField(max_length=100, blank=True, null=True, default="")
   p5 = models.CharField(max_length=100, blank=True, null=True, default="")
   p6 = models.CharField(max_length=100, blank=True, null=True, default="")
   def __str__(self):
      return str(self.Room_no.room_no) + ',' + str(self.Room_no.get_block_display())

class Master_final(models.Model):
   day1 = 1
   day2 = 2
   day3 = 3
   day4 = 4
   day5 = 5
   day6 = 6
   Type_Day = (
       (day1, 'Monday'),
       (day2, 'Tuesday'),
       (day3, 'Wednesday'),
       (day4, 'Thrusday'),
       (day5, 'Friday'),
       (day6, 'Saturday'),
   )
   STATUS_INACTIVE = 0
   STATUS_ACTIVE = 1

   STATUS_CHOICES = (
       (STATUS_INACTIVE, 'Inactive'),
       (STATUS_ACTIVE, 'Active')
   )
   day_type = models.SmallIntegerField(choices=Type_Day, default=day1)
   sec = models.ForeignKey(Sec, on_delete=models.CASCADE)
   p1 = models.CharField(max_length=1000, blank=True, null=True, default="")
   p2 = models.CharField(max_length=1000, blank=True, null=True, default="")
   p3 = models.CharField(max_length=1000, blank=True, null=True, default="")
   p4 = models.CharField(max_length=1000, blank=True, null=True, default="")
   p5 = models.CharField(max_length=1000, blank=True, null=True, default="")
   p6 = models.CharField(max_length=1000, blank=True, null=True, default="")
   status = models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_INACTIVE)
   def __str__(self):
      return str(self.sec.Section) + ',' + str(self.sec.sem.sem) + ',' + str(self.sec.sem.department.department_initials)

class Lab_final(models.Model):
   day1 = 1
   day2 = 2
   day3 = 3
   day4 = 4
   day5 = 5
   day6 = 6
   Type_Day = (
       (day1, 'Monday'),
       (day2, 'Tuesday'),
       (day3, 'Wednesday'),
       (day4, 'Thrusday'),
       (day5, 'Friday'),
       (day6, 'Saturday'),
   )
   lab_no = models.ForeignKey(Lab, on_delete=models.CASCADE)
   sec = models.CharField(max_length=100, blank=True, default="", null=True)
   day_type = models.SmallIntegerField(choices=Type_Day, default=day1)
   p1 = models.CharField(max_length=100, blank=True, null=True, default="")
   p2 = models.CharField(max_length=100, blank=True, null=True, default="")
   p3 = models.CharField(max_length=100, blank=True, null=True, default="")
   p4 = models.CharField(max_length=100, blank=True, null=True, default="")
   p5 = models.CharField(max_length=100, blank=True, null=True, default="")
   p6 = models.CharField(max_length=100, blank=True, null=True, default="")
   def __str__(self):
      return str(self.lab_no.lab_no) + ',' + str(self.lab_no.get_block_display())
