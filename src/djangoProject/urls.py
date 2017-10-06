from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from service import views

urlpatterns = [

	url(r'^weather/', include('weather.urls')),
	url(r'^service/', include('service.urls')),
    url(r'^calculate/', include('calculate.urls')),   
    url(r'^admin/', admin.site.urls),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
