from django.contrib import admin
from .models import *


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price',)
    search_fields = ('id', 'name')


admin.site.register(Category),
admin.site.register(Car, CarAdmin),
