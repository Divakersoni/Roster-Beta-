# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Teacher
from models import Department
from models import Subject

class Teacher_Admin(admin.ModelAdmin):
	list_display = ('id', 'designation', 'teacher_name', 'department_name')
	list_per_page = 100
	search_fields = ('id', 'teacher_initials', 'subject1')
	ordering = ['id']
	list_filter = ['id']
	fieldsets = [
    ('Name', {'fields': ['teacher_name']}),
    ('Date of birth', {'fields': ['DOB']}),
    ('Shift', {'fields': ['shift']}),
    ('Department', {'fields': ['department_name']}),
    ('Subject 1', {'fields': ['subject1']}),
    ('Subject 2', {'fields': ['subject2']}),
    ('Subject 3', {'fields': ['subject3']}),
    ('Subject 4', {'fields': ['subject4']}),
    ('Teaching Hours per Week', {'fields': ['teaching_hours_per_week']}),
    ('Teaching Hours a Day Subject 1', {'fields': ['teaching_hours_a_day_subject1']}),
    ('Teaching Hours a Day Subject 2', {'fields': ['teaching_hours_a_day_subject2']}),
    ('Teaching Hours a Day Subject 3', {'fields': ['teaching_hours_a_day_subject3']}),
    ('Teaching Hours a Day Subject 4', {'fields': ['teaching_hours_a_day_subject4']}),
    ('Designation', {'fields': ['designation']}),
    ('Initials', {'fields': ['teacher_initials']}),
    ('Total teaching hours a day', {'fields': ['total_teaching_hours_a_day']}),
    ]

class Department_Admin(admin.ModelAdmin):
	list_display = ('id', 'department_name')
	list_per_page = 100
	search_fields = ('id', 'department_initials', 'subject1')
	ordering = ['id']
	list_filter = ['id']
	fieldsets = [
    ('Department', {'fields': ['department_name']}),
    ('Initials', {'fields': ['department_initials']}),
    ('Block', {'fields': ['block']}),
    ]

class Subject_Admin(admin.ModelAdmin):
	list_display = ('id', 'subject_name', 'type_subject', 'teaching_hours_a_day','teaching_hours_per_week')
	list_per_page = 100
	search_fields = ('id', 'subject_initials', 'subject1')
	ordering = ['id']
	list_filter = ['id']
	fieldsets = [
    ('Subject', {'fields': ['subject_name']}),
    ('Initials', {'fields': ['subject_initials']}),
    ('Code', {'fields': ['subject_code']}),
    ('Semester', {'fields': ['semester']}),
    ('Type', {'fields': ['type_subject']}),
    ('Hours per Week', {'fields': ['teaching_hours_per_week']}),
    ('Hours a Day', {'fields': ['teaching_hours_a_day']}),
    ('Department name', {'fields': ['department_name']}),
    ]
admin.site.register(Teacher, Teacher_Admin)
admin.site.register(Department, Department_Admin)
admin.site.register(Subject, Subject_Admin)
admin.site.disable_action('delete_selected')
