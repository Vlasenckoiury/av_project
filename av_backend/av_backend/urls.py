from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('av_car.urls')),
    path('', include(CarListCreate.as_view()), name='list_car'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
