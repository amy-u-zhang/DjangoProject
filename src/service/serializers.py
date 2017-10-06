from rest_framework import serializers
from .models import Temperatures

class TemperaturesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Temperatures
		#fields = ('latitude', 'average')
		fields = '__all__'