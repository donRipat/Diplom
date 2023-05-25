from ..models import *


def new_booking_handle(booking: Booking) -> bool:
    print(f"-------------------------------new_booking.py-------------------------------- ")
    print(f"new_booking_handle(booking.scheduled_route = {booking.scheduled_route})")
    if try_existing_drives(booking):
        return True
    if create_drive(booking):
        return True
    return False


def try_existing_drives(booking: Booking) -> bool:
    print(f"try_existing_drives(booking.scheduled_route = {booking.scheduled_route})")
    drives = Drive.objects.filter(
        scheduled_route=booking.scheduled_route,
        date=booking.date,
    )
    print('drives = ', drives)
    for drive in drives:
        pass_num = len(drive.passengers.all())
        if pass_num < drive.car.sits - 1:
            Passenger.objects.create(
                booking=booking,
                drive=drive,
            )
            return True
    return False


def create_drive(booking: Booking)-> bool:
    print(f"create_drive(booking.scheduled_route = {booking.scheduled_route})")
    busy_cars = Drive.objects.filter(
        date=booking.date,
    ).values_list('car')
    busy_drivers = Drive.objects.filter(
        date=booking.date,
    ).values_list('driver')
    free_drivers = Driver.objects.exclude(id__in=busy_drivers)
    free_cars = Car.objects.exclude(id__in=busy_cars)
    if (not free_cars) or (not free_drivers):
        return False
    print(f"free_drivers = {free_drivers}")
    print(f"free_cars = {free_cars}")
    created_drive = Drive.objects.create(
        driver=free_drivers[0],
        car=free_cars[0],
        date=booking.date,
        scheduled_route=booking.scheduled_route,
    )
    Passenger.objects.create(
        booking=booking,
        drive=created_drive,
    )
    return True

