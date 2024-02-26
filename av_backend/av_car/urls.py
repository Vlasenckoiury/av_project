from django.urls import path
from .views import CarListCreate


urlpatterns = [
    path('car', CarListCreate.as_view(), name='list_car')
]
