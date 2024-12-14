from rest_framework import serializers
from djangoapi.models import CarData

class CarDataSerializer(serializers.ModelSerializer):
  class Meta:
    model = CarData
    fields = ['id', 'model', 'year']