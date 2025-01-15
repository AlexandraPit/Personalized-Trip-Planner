from django.shortcuts import render

def homepage(request):
    return render(request, 'home/homepage.html')
def destination(request):
    return render(request, 'home/destination.html')
def userInput(request):
    return render(request, 'home/userInput.html')