from rest_framework.routers import DefaultRouter
from .views import CarViewSet, car_list
from django.urls import path, include

router = DefaultRouter()
router.register(r'api/car', CarViewSet, 'cars')

# urlpatterns = router.urls
urlpatterns = [
    path('', car_list, name='mymodel-list'),
    path('', include(router.urls)),
]
