from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from .models import Temperature

# Create your views here.
def index(request):
	all_temperatures = Temperature.objects.all()
	#template = loader.get_template('calculate/index.html')
	context = {
	    'all_temperatures' : all_temperatures,
	}
	#return HttpResponse(template.render(context, request))
	return render(request, 'calculate/index.html', context)

def detail(request, temperature_id=None):
	return HttpResponse("<h2>Details for temperature: " + str(temperature_id) + "</h2>")
