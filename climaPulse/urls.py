
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('analytics/', views.analytics, name='analytics'),
    path('locations/', views.location, name='locations'),
    path('blog/', views.blog, name='blog'),
    path('forecast/', views.forecast, name='forecast'),
    path('calendar/', views.calendar, name='calendar'),
    path('create_blog/', views.create_blog_post, name='create_blog'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    #weather data API
    path('get_weather_data/', views.get_weather_data, name='get_weather_data'),
    path('add_weather_data/', views.add_weather_data, name='add_weather_data'),
    path('delete_weather_data/<int:id>/', views.delete_weather_data, name='delete_weather_data'),
    path('update_weather_data/<int:id>/', views.update_weather_data, name='update_weather_data'),
    path('chart-data/', views.get_chart_data, name='chart-data'),

]   
