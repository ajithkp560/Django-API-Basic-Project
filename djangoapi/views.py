from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CarData
from djangoapi.serializers import CarDataSerializer

class CreateCar(APIView):
  def post(self, request):
    serializer = CarDataSerializer(data=request.data)
    if serializer.is_valid():
      car = serializer.save()
      return Response(CarDataSerializer(car).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListCar(APIView):
  def get(self, request):
    cars = CarData.objects.all()
    serializer = CarDataSerializer(cars, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
class UpdateCar(APIView):
  def patch(self, request, id):
    try:
      car = CarData.objects.get(id=id)
    except CarData.DoesNotExist:
      return Response([], status=status.HTTP_404_NOT_FOUND)
    if not request.data:
      return Response([], status=status.HTTP_400_BAD_REQUEST)
    serializer = CarDataSerializer(car, data=request.data, partial=True)
    if serializer.is_valid():
      car = serializer.save()
      return Response(CarDataSerializer(car).data, status=status.HTTP_200_OK)
    else:
      return Response([], status=status.HTTP_400_BAD_REQUEST)
    
class DeleteCar(APIView):
  def delete(self, request, id):
    try:
      car = CarData.objects.get(id=id)
    except CarData.DoesNotExist:
      return Response([], status=status.HTTP_404_NOT_FOUND)
    car.delete()
    return Response(dict(message='Car deleted'), status=status.HTTP_204_NO_CONTENT)