from rest_framework import generics
from .serializers import *
from .models import *
import datetime

now = datetime.datetime.now()


class CarListCreate(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# @api_view(['GET', 'POST'])
# def car_list(request):
#     queryset = Car.objects.all()
#     return queryset