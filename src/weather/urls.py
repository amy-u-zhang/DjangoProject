from django.conf.urls import url
from . import views

urlpatterns = [

    # /weather/latitude30/longitude40/filters=noaa,weatherdotcom,accuweather,testweather/
    url(r'^latitude(?P<latitude>\d+)/longitude(?P<longitude>\d+)/filters=(?P<filters>[^/]+)/$',
        views.get_avg_temperature, name='get_avg_temperature'),


]
