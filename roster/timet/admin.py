# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Room_final,Teacher_final,Master_final,Lab_final
class Lab_final_Admin(admin.ModelAdmin):
	list_display = ('id', 'lab_no', 'day_type','p1','p2','p3','p4','p5','p6','sec')
	list_per_page = 100
	search_fields = ('id', 'lab_no')
	ordering = ['id']
	list_filter = ['id']
	fieldsets = [
    ('Lab no', {'fields': ['lab_no']}),
    ('Sec', {'fields': ['sec']}),
    ('Day', {'fields': ['day_type']}),
    ('P1', {'fields': ['p1']}),
    ('P2', {'fields': ['p2']}),
    ('P3', {'fields': ['p3']}),
    ('P4', {'fields': ['p4']}),
    ('P5', {'fields': ['p5']}),
    ('P6', {'fields': ['p6']}),
    ]
class Master_final_Admin(admin.ModelAdmin):
	list_display = ('id', 'sec', 'day_type','p1','p2','p3','p4','p5','p6')
	list_per_page = 100
	search_fields = ('id', 'sec')
	ordering = ['id']
	list_filter = ['id']
	fieldsets = [
    ('Section', {'fields': ['sec']}),
    ('Day', {'fields': ['day_type']}),
    ('P1', {'fields': ['p1']}),
    ('P2', {'fields': ['p2']}),
    ('P3', {'fields': ['p3']}),
    ('P4', {'fields': ['p4']}),
    ('P5', {'fields': ['p5']}),
    ('P6', {'fields': ['p6']}),
    ('Status', {'fields': ['status']}),
    ]
class Teacher_final_Admin(admin.ModelAdmin):
	list_display = ('id','teacher_name', 'day_type', 'teaching_hours' ,'p1','p2','p3','p4','p5','p6')
	list_per_page = 100
	search_fields = ('id', 'teacher_name')
	ordering = ['id']
	list_filter = ['id']
	fieldsets = [
    ('Teacher name', {'fields': ['teacher_name']}),
    ('Teaching hours', {'fields': ['teaching_hours']}),
    ('Day', {'fields': ['day_type']}),
    ('P1', {'fields': ['p1']}),
    ('P2', {'fields': ['p2']}),
    ('P3', {'fields': ['p3']}),
    ('P4', {'fields': ['p4']}),
    ('P5', {'fields': ['p5']}),
    ('P6', {'fields': ['p6']}),
    ]
class Room_final_Admin(admin.ModelAdmin):
	list_display = ('id','Room_no','p1','p2','p3','p4','p5','p6')
	list_per_page = 100
	search_fields = ('id', 'Room_no')
	ordering = ['id']
	list_filter = ['id']
	fieldsets = [
    ('Room no', {'fields': ['Room_no']}),
    ('Day', {'fields': ['day_type']}),
    ('P1', {'fields': ['p1']}),
    ('P2', {'fields': ['p2']}),
    ('P3', {'fields': ['p3']}),
    ('P4', {'fields': ['p4']}),
    ('P5', {'fields': ['p5']}),
    ('P6', {'fields': ['p6']}),
    ]
admin.site.register(Room_final,Room_final_Admin)
admin.site.register(Lab_final,Lab_final_Admin)
admin.site.register(Teacher_final,Teacher_final_Admin)
admin.site.register(Master_final,Master_final_Admin)