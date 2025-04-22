from django.contrib import admin
from .models import BlogPost, WeatherData

# Register your models here.

admin.site.register(BlogPost)
admin.site.register(WeatherData)