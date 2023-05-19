from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100, blank=True)
    parent_city_id = models.PositiveIntegerField(default=0)
    est_time_ufa = models.DecimalField(max_digits=4, decimal_places=2)
    est_time_addition = models.DecimalField(max_digits=4, decimal_places=2)
    dist_ufa = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(999)])
    dist_parent = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(99)])
    price_addition = models.PositiveIntegerField(default=100, validators=[
        MinValueValidator(0),
        MaxValueValidator(999)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Города'


class Route(models.Model):
    start_city = models.ForeignKey(City, related_name='starting_routes',
                                   on_delete=models.CASCADE)
    finish_city = models.ForeignKey(City, related_name='finishing_routes',
                                    on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=1000, validators=[
        MinValueValidator(100),
        MaxValueValidator(9999)])

    def __str__(self):
        return f'{self.start_city}—{self.finish_city}: ({self.price} руб.)'

    class Meta:
        unique_together = ('start_city', 'finish_city')
        verbose_name_plural = 'Маршруты'


class Schedule(models.Model):
    time = models.TimeField(auto_now=False)
    route = models.ForeignKey(Route, related_name='times',
                              on_delete=models.CASCADE)

    def __str__(self):
        return {
            'route': self.route,
            'time': self.time,
        }

    class Meta:
        verbose_name_plural = 'Маршруты — время'


class Booking(models.Model):
    client_phone = models.CharField(max_length=20)
    client_name = models.CharField(max_length=100, blank=True, default='')
    start_city = models.ForeignKey(City, related_name='starting_bookings',
                                   on_delete=models.CASCADE)
    finish_city = models.ForeignKey(City, related_name='finishing_bookings',
                                    on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.PROTECT)
    total_price = models.PositiveIntegerField(default=1000, validators=[
        MinValueValidator(100),
        MaxValueValidator(9999)])
    min_time = models.TimeField(auto_now=False)
    max_time = models.TimeField(auto_now=False)
    start_address = models.CharField(max_length=250, blank=False)
    finish_address = models.CharField(max_length=250, blank=False)
    
    def __str__(self):
        return {
            'client_phone': self.client_phone,
            'client_name': self.client_name,
            'start_city': self.start_city,
            'finish_city': self.finish_city,
            'route': self.route,
            'total_price': self.total_price,
            'min_time': self.min_time,
            'max_time': self.max_time,
            'start_address': self.start_address,
            'finish_address': self.finish_address,
        }

    class Meta:
        verbose_name_plural = 'Заказы'


class Driver(models.Model):
    phone = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Водители'


class Car(models.Model):
    model = models.CharField(max_length=50, blank=False)
    plate = models.CharField(max_length=15, blank=False)
    sits = models.PositiveIntegerField(default=5, validators=[
        MinValueValidator(5),
        MaxValueValidator(9)])

    def __str__(self):
        return str({
            'model': self.model,
            'plate': self.plate,
            'sits': self.sits,
        })

    class Meta:
        verbose_name_plural = 'Автомобили'


class Drive(models.Model):
    car = models.ForeignKey(Car, related_name='drives',
                            on_delete=models.PROTECT)
    driver = models.ForeignKey(Driver, related_name='drives',
                               on_delete=models.CASCADE)
    scheduled_route = models.ForeignKey(Route, related_name='drives',
                                        on_delete=models.CASCADE)

    def __str__(self):
        return {
            'route': self.scheduled_route,
            'driver': self.driver,
            'car': self.car,
        }

    class Meta:
        verbose_name_plural = 'Поездки'
        unique_together = ('scheduled_route', 'driver', 'car')


class Passenger(models.Model):
    drive = models.ForeignKey(Drive, related_name='passengers',
                              on_delete=models.PROTECT)
    booking = models.OneToOneField(Booking, related_name='passenger',
                                   on_delete=models.CASCADE)
    est_dep_time = models.TimeField(auto_now=False)

    def __str__(self):
        return f'{self.booking} {self.est_dep_time} {self.drive}'

    class Meta:
        verbose_name_plural = 'Пассажиры'


class Stops(models.Model):
    drive = models.ForeignKey(Drive, related_name='stops',
                              on_delete=models.CASCADE)
    city = models.ForeignKey(City, related_name='stops',
                             on_delete=models.CASCADE)
    address = models.CharField(max_length=250, blank=False)

    def __str__(self):
        return {
            'drive': self.drive,
            'city': self.city,
            'address': self.address,
        }

    class Meta:
        verbose_name_plural = 'Остановки'
