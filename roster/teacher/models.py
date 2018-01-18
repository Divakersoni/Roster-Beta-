# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Department(models.Model):
	Block_A = 0
	Block_B = 1
	Block_C = 2
	Block_D = 3
	Type_Block = (
        (Block_A,'A'),
        (Block_B,'B'),
        (Block_C,'C'),
        (Block_D,'D')
		)
	block = models.SmallIntegerField(choices=Type_Block, default=Block_A)
	department_name = models.CharField(max_length=100)
	department_initials = models.CharField(max_length=10)
	def __str__(self):
		return str(self.department_name) + "," + str(self.department_initials)


class Subject(models.Model):
	Theory = 0
	Lab = 1
	Type_Subject = (
    	(Theory,'Theory'),
    	(Lab,'Lab')
    	) 
	subject_name = models.CharField(max_length=100)
	subject_initials = models.CharField(max_length=10)
	type_subject = models.SmallIntegerField(choices=Type_Subject, default=Theory)
	semester = models.SmallIntegerField()
	subject_code = models.CharField(max_length=10)
	department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
	teaching_hours_per_week = models.SmallIntegerField()
	teaching_hours_a_day = models.SmallIntegerField()
	def __str__(self):
		return self.subject_name

class Teacher(models.Model):
    shift_1 = 0
    shift_2 = 1
    Type_shift = (
        (shift_1,"I"),
        (shift_2,"II")
    )
    teacher_name = models.CharField(max_length=100)
    teacher_initials = models.CharField(max_length=10,blank=True)
    DOB = models.CharField(max_length=10,blank=True)
    designation = models.CharField(max_length=100)
    teaching_hours_per_week = models.SmallIntegerField()
    shift= models.SmallIntegerField(choices=Type_shift,default=shift_1)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    subject1 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject1')
    subject2 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject2',blank=True, null=True)
    subject3 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject3',blank=True, null=True)
    subject4 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject4',blank=True, null=True)
    teaching_hours_a_day_subject1 = models.SmallIntegerField(default=0)
    teaching_hours_a_day_subject2 = models.SmallIntegerField(default=0,blank=True,null=True)
    teaching_hours_a_day_subject3 = models.SmallIntegerField(default=0,blank=True,null=True)
    teaching_hours_a_day_subject4 = models.SmallIntegerField(default=0,blank=True,null=True)
    total_teaching_hours_a_day = models.SmallIntegerField(default=4)
    def __str__(self):
		return self.teacher_name

