from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, BlogPostForm
from .models import BlogPost, WeatherData
from django.utils.timezone import localtime

API_TOKEN = "_token_"

# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def analytics(request):
    return render(request, 'analytics.html', {})


def location(request):
    return render(request, 'Locations.html', {}) 


def blog(request):   
    blog_posts = BlogPost.objects.all().order_by('-created_at')

    return render(request, 'blog.html', {'blog_posts': blog_posts})     
    


def forecast(request):
    return render(request, 'forecast.html', {})


def calendar(request):
    return render(request, 'calendar.html', {}) 


def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.user = request.user
            blog_post.save()
        return render(request, 'create_blog.html', {'message': 'Blog post created successfully!'})
    else:
        form = BlogPostForm()
    return render(request, 'create_blog.html', {'form': form})    


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index') 
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# weather data functions 
def get_weather_data(request):
    latest = WeatherData.objects.latest('date_time')  # Get the newest by timestamp
    data = {
        'pressure': latest.pressure,
        'wind_direction': latest.wind_direction,
        'temperature': latest.temperature,
        'humidity': latest.humidity,
    }
    return JsonResponse(data)


def add_weather_data(request):
    if request.method == 'POST':
        # token = request.headers.get('Authorization')

        # if token != f"Token {API_TOKEN}":
        #     return JsonResponse({'status': 'fail', 'message': 'Invalid token'}, status=403)

        wind_direction = request.POST.get('wind_direction')
        pressure = request.POST.get('pressure')
        temperature = request.POST.get('temperature')
        humidity = request.POST.get('humidity')

        if not all([wind_direction, pressure, temperature, humidity]):
            return JsonResponse({'status': 'fail', 'message': 'Missing data'}, status=400)

        WeatherData.objects.create(
            wind_direction=wind_direction,
            pressure=float(pressure),
            temperature=float(temperature),
            humidity=float(humidity)
        )

        return JsonResponse({'status': 'success', 'message': 'Data saved'})
    else:
        return JsonResponse({'status': 'fail', 'message': 'Only POST allowed'}, status=405)
    

def get_chart_data(request):
    latest_entries = WeatherData.objects.order_by('-date_time')[:15]  # Last 20 readings
    latest_entries = reversed(latest_entries)  # oldest first

    labels = []
    temperatures = []
    humidities = []
    pressures = []

    for entry in latest_entries:
        labels.append(entry.date_time.strftime('%H:%M:%S'))
        temperatures.append(entry.temperature)
        humidities.append(entry.humidity)
        pressures.append(entry.pressure)

    data = {
        'labels': labels,
        'temperature': temperatures,
        'humidity': humidities,
        'pressure': pressures,
    }

    return JsonResponse(data)
    

def delete_weather_data(request, weather_data_id):
    weather_data = WeatherData.objects.get(id=weather_data_id)
    weather_data.delete()
    return redirect('weather_data')  # Redirect to the weather data page after deleting


def update_weather_data(request, weather_data_id):  
    weather_data = WeatherData.objects.get(id=weather_data_id)
    if request.method == 'POST':
        weather_data.temperature = request.POST['temperature']
        weather_data.humidity = request.POST['humidity']
        weather_data.pressure = request.POST['pressure']
        weather_data.wind_direction = request.POST['wind_direction']
        weather_data.save()
        return redirect('weather_data')  # Redirect to the weather data page after updating

    return render(request, 'update_weather_data.html', {'weather_data': weather_data})



