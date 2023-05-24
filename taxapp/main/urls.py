from django.contrib import admin
from django.urls import path
from . import views
from .views.employees import employees
from .views.cars import cars
from .views.routes import routes
from .views.cities import cities
from .views.clients import clients
from .views.areas import areas
from .views.test import test
from .views.choose_route import choose

urlpatterns = [
    path('', views.clients.clients),
    
    path('choose-route', views.choose_route.choose),
    path('route/<int:id>', views.choose_route.route_edit),
    path('route/<int:id>/add-time', views.choose_route.add),
    path('route/<int:r_id>/delete-time/<int:t_id>', views.choose_route.delete),

    
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
    
    path('areas', views.areas.areas),
    path('area/add', views.areas.add),
    path('area/delete/<int:id>', views.areas.delete),
    
    path('routes', views.routes.routes),
    path('route/add', views.routes.add),
    path('route/delete/<int:id>', views.routes.delete),

    path('test', views.test.test)
]
