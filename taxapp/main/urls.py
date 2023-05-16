from django.contrib import admin
from django.urls import path
from . import views
from .views.schedule import schedule
from .views.employees import employees
from .views.cars import cars
from .views.routes import routes
from .views.cities import cities
from .views.clients import clients

urlpatterns = [
    path('', views.schedule.schedule),
    path('schedule', views.schedule.schedule),
    path('employees', views.employees.employees),
    path('cars', views.cars.cars),
    path('clients', views.clients.clients),
    path('cities', views.cities.cities),
    path('routes', views.routes.routes),
]
