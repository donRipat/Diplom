from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(ScheduledRoute)
admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(Drive)

admin.site.register(Booking)
admin.site.register(Stops)
admin.site.register(Passenger)
admin.site.register(City)

admin.site.register(Route)
admin.site.register(Area)
