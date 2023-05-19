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
    path('employee/add', views.employees.add),
    path('employee/delete/<int:id>', views.employees.delete),
    
    path('cars', views.cars.cars),
    path('car/add', views.cars.add),
    path('car/delete/<int:id>', views.cars.delete),
    
    path('clients', views.clients.clients),
    
    path('cities', views.cities.cities),
    path('city/add', views.cities.add),
    path('city/delete/<int:id>', views.cities.delete),
    
    path('routes', views.routes.routes),
    path('route/add', views.routes.add),
    path('route/delete/<int:id>', views.routes.delete),
]
