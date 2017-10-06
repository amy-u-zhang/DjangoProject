# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Temperature(models.Model):
	city = models.CharField(max_length=100, default="")
	latitude = models.IntegerField(default=None, null=True)
	longitute = models.IntegerField(default=None, null=True)
	noaa = models.FloatField(default=None, null=True)
	weather_com = models.FloatField(default=None, null=True)
	accuweather = models.FloatField(default=None, null=True)

	def __str__(self):
		return  self.city

class Average(models.Model):
	city = models.ForeignKey(Temperature, on_delete=models.CASCADE)
	average_temperature = models.FloatField(default=None, null=True)