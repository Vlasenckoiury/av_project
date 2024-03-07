from .models import Car
from .serializers import CarSerializer
from rest_framework import viewsets, permissions
from django.shortcuts import render


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarSerializer


def car_list(request):
    car = Car.objects.all()
    return render(request, 'av_car/index.html', {'car': car})
