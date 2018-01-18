# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from teacher.models import Department
class Sem(models.Model):
    sem = models.SmallIntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.sem) + ',' + str(self.department.department_initials)



class Sec(models.Model):
    sem = models.ForeignKey(Sem, on_delete=models.CASCADE)
    Section = models.CharField(max_length=10)
    def __str__(self):
        return str(self.sem.sem) + ',' + str(self.sem.department.department_initials) + ',' + str(self.Section)