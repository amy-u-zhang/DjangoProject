from django.db import models


class Temperatures(models.Model):
	latitude = models.IntegerField(default=None, null=True)
	longitute = models.IntegerField(default=None, null=True)
	noaa = models.FloatField(default=None, null=True)
	weather_com = models.FloatField(default=None, null=True)
	accuweather = models.FloatField(default=None, null=True)
	average = models.FloatField(default=None, null=True)

	def __str__(self):
		return str(self.average)