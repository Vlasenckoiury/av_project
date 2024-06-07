from rest_framework.routers import DefaultRouter
from .views import CarViewSet
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'car', CarViewSet, 'cars')

# urlpatterns = router.urls
urlpatterns = [
    # path('', car_list, name='mymodel-list'),
    path('', include(router.urls)),
    path('user', views.UserView.as_view(), name='user'),
    path('login', views.UserLogin.as_view(), name='login'),
    path('logout', views.UserLogout.as_view(), name='logout'),
    path('register', views.UserRegister.as_view(), name='register'),
]
