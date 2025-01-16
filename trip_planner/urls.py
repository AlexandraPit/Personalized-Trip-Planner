"""
URL configuration for trip_planner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from home import views
from home.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage, name='homepage'),
    path('destination/', views.destination, name='destination'),
    path('userInput/', views.userInput, name='userInput'),
    path('activities/', views.activities, name='activities'),
    path('itinerary/', views.itinerary, name='itinerary'),
    path('custom-admin/login/', views.admin_login, name='admin_login'),
    path('custom-admin/logout/', views.admin_logout, name='admin_logout'),
    path('custom-admin/', views.admin_page, name='admin_page'),
    path('custom-admin/add', views.add_activity, name='add_activity'),
    path('custom-admin/edit/<int:activity_id>/', views.edit_activity, name='edit_activity'),
    path('custom-admin/delete/<int:activity_id>/', views.delete_activity, name='delete_activity'),
    path('plan_trip/', views.plan_trip, name='plan_trip'),
    path('search_cities/', views.search_cities, name='search_cities'),
    path('activities/<str:city_name>/', views.city_activities, name='city_activities'),
    path('activities_in_city/<int:city_id>/', views.activities_in_city, name='activities_in_city'),
]
