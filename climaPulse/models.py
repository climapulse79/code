from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    isVisible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class WeatherData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    wind_direction = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mbale {self.temperature}°C"