from django.contrib import admin
from django.urls import path
from . import views
from .views.employees import employees
from .views.cars import cars
from .views.routes import routes
from .views.cities import cities
from .views.bookings import bookings
from .views.areas import areas
from .views.test import test
from .views.choose_route import choose
from .views.drives import drives
from .views.drive_details import drive_details

urlpatterns = [
    path('', views.bookings.bookings),
    
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
    
    path('bookings', views.bookings.bookings),
    path('booking/add', views.bookings.add),
    path('booking/delete/<int:id>', views.bookings.delete),
    
    path('cities', views.cities.cities),
    path('city/add', views.cities.add),
    path('city/delete/<int:id>', views.cities.delete),
    
    path('areas', views.areas.areas),
    path('area/add', views.areas.add),
    path('area/delete/<int:id>', views.areas.delete),
    
    path('routes', views.routes.routes),
    path('route/add', views.routes.add),
    path('route/delete/<int:id>', views.routes.delete),
    
    path('drives', views.drives.drives),
    path('drive/<int:id>', views.drive_details.drive_details),

    path('test', views.test.test)
]
