from django.http import HttpResponse

from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Temperatures
from .serializers import TemperaturesSerializer
from . import weatherServices
from .weatherServices import  Average
import requests
from django.http import JsonResponse


# Lists all temperatures
# /service/
class TemperatureList(APIView):
	
	def get(self, request):
		temperatures = Temperatures.objects.all()
		serializer = TemperaturesSerializer(temperatures, many=True)
		return Response(serializer.data)

	def post(self):
		pass


# get temperature from a specific weather site
# /service/noaa/
def get_temperature(request, service=None):
	url = ''
	if (service == 'noaa'):
		url = 'http://127.0.0.1:5000/noaa?latlon=44,33'
		#response = requests.get(url)
	elif (service == 'accuweather'):
		url = 'http://127.0.0.1:5000/accuweather?latitude=44&longitude=33'
		#response = requests.get(url)
	elif (service == 'weatherdotcom'):
		url = 'http://127.0.0.1:5000/weatherdotcom {"lat":33.3,"lon":44.4}'
		#response = requests.post(url)

	response = requests.get(url)
	if (response.status_code == 200):
		data = response.json()
	else:
		data = {}

	return JsonResponse(data)


# /service/latitude30/longitude40/filters=noaa,weatherdotcom,accuweather,testweather/
def get_avg_temperature(request, latitude=None, longitude=None, filters=None):
	average = Average.get_avg_temperature(filters)

	return JsonResponse(average)



