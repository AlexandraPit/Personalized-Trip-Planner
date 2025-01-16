from django.shortcuts import render

def homepage(request):
    return render(request, 'home/homepage.html')
def destination(request):
    return render(request, 'home/destination.html')
def userInput(request):
    return render(request, 'home/userInput.html')
def activities(request):
    return render(request, 'home/activities.html')
def itinerary(request):
    return render(request, 'home/itinerary.html')