from . import weatherServices
from django.http import JsonResponse



# /weather/latitude30/longitude40/filters=noaa,weatherdotcom,accuweather,testweather/
def get_avg_temperature(request, latitude=None, longitude=None, filters=None):

	average = weatherServices.get_avg_temperature(filters)

	return JsonResponse(average)



