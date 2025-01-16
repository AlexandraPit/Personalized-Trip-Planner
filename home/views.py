from django.core.checks import messages
from django.db import connection
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import City, Activity, Image  # Import your Activity model
def homepage(request):
    return render(request, 'home/homepage.html')
def destination(request):
    return render(request, 'home/destination.html')
def userInput(request):
    return render(request, 'home/userInput.html')
def activities(request):
    return render(request, 'home/activities.html')
def itinerary(request):
    if request.method == 'POST':
        selected_activity_ids = request.POST.getlist('activity_ids')
        if selected_activity_ids:
            # Process the selected activity IDs (e.g., save to session or database)
            return render(request, 'home/itinerary.html', {'selected_activities': selected_activity_ids})
        else:
            return HttpResponse("No activities were selected.")

def admin_page(request):
    if not request.session.get('is_admin'):  # Check if admin is logged in
        return redirect('admin_login')

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM activity")
        activities = cursor.fetchall()
        columns = [col[0] for col in cursor.description]

    return render(request, 'admin.html', {'activities': activities, 'columns': columns})

def add_activity(request):
    if request.method == 'POST':
        # Get data from the form
        title = request.POST['title']
        description = request.POST['description']
        opening_hour = request.POST['opening_hour']
        closing_hour = request.POST['closing_hour']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        city_id = request.POST['city_id']
        image_id = request.POST['image_id']

        # Insert the new activity into the database
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO activity (title, description, opening_hour, closing_hour, latitude, longitude, city_id, image_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, [title, description, opening_hour, closing_hour, latitude, longitude, city_id, image_id])
        return redirect('admin_page')
 # Handle GET requests
    if request.method == 'GET':
        return render(request, 'add_activity.html')

def delete_activity(request, activity_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM activity WHERE activity_id=%s", [activity_id])
    return redirect('admin_page')


def edit_activity(request, activity_id):
    if request.method == 'POST':
        # Get updated data from the form
        title = request.POST['title']
        description = request.POST['description']
        opening_hour = request.POST['opening_hour']
        closing_hour = request.POST['closing_hour']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        city_id = request.POST['city_id']
        image_id = request.POST['image_id']

        # Update the activity in the database
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE activity 
                SET title=%s, description=%s, opening_hour=%s, closing_hour=%s,
                    latitude=%s, longitude=%s, city_id=%s, image_id=%s
                WHERE activity_id=%s
            """, [title, description, opening_hour, closing_hour, latitude, longitude, city_id, image_id, activity_id])
        return redirect('admin_page')

    # Fetch the current activity data
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM activity WHERE activity_id=%s", [activity_id])
        columns = [col[0] for col in cursor.description]
        activity = dict(zip(columns, cursor.fetchone()))

    return render(request, 'edit_activity.html', {'activity': activity})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Hardcoded admin credentials
        if username == 'admin' and password == 'admin':
            request.session['is_admin'] = True  # Set a session variable to indicate admin is logged in
            return redirect('admin_page')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'admin_login.html')

def admin_logout(request):
    request.session.flush()  # Clear all session data
    return redirect('admin_login')


def plan_trip(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM city")
        cities = cursor.fetchall()

    return render(request, 'home/destination.html', {'cities': cities})
def search_cities(request):
    query = request.GET.get('query', '')  # Get the search query from the request
    if query:
        cities = City.objects.filter(name__icontains=query)  # Match city names with the query
        city_names = [city.name for city in cities]  # Extract city names
    else:
        city_names = []

    return JsonResponse({'cities': city_names})
def city_activities(request, city_name):
    # Filter activities by the city name (through the related City model)
    activitiesFetched = Activity.objects.filter(city__name__icontains=city_name)

    return render(request, 'home/city_activities.html', {
        'city_name': city_name,
        'activities': activitiesFetched
    })


def activities_in_city(request, city_id):
    # Fetch the selected city object using the city_id
    selected_city = City.objects.get(city_id=city_id)

    # Filter activities by the selected city's ID
    activities_city = Activity.objects.filter(city__city_id=city_id)



    return render(request, 'home/activities_in_city.html', {
        'selected_city': selected_city,
        'activities': activities_city,
        'city_name': selected_city.name
    })
