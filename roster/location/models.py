# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from semclass.models import Sec
from teacher.models import Subject
class ClassRoom(models.Model):
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
	room_no = models.CharField(max_length=10)
	sec1 = models.ForeignKey(Sec, on_delete=models.CASCADE, related_name='sec1', blank=True, null=True)
	sec2 = models.ForeignKey(Sec, on_delete=models.CASCADE, related_name='sec2', blank=True, null=True)
	alt_name = models.CharField(max_length=10, default='LH1', null = True)
	def __str__(self):
		return self.room_no + ','+ str(self.get_block_display()) +','

class Lab(models.Model):
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
	block = models.SmallIntegerField(choices=Type_Block, default = Block_A)
	lab_no = models.CharField(max_length=10)
	alt_name = models.CharField(max_length=10, default='cp1', null = True)
	def __str__(self):
		return self.lab_no + '('+ str(self.get_block_display()) +')'