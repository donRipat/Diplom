from .models import *
from django import forms


class CarForm(forms.Form):
    model = forms.CharField(label="Цвет, марка, модель", max_length=50)
    plate = forms.CharField(label='Регистрационный номер', max_length=15)
    sits = forms.IntegerField(label='Количество сидений', initial=5, max_value=9, min_value=2)

    class Meta:
        model = Car
        exclude = []


class DriverForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    phone = forms.CharField(label='Телефон', max_length=20)

    class Meta:
        model = Driver
        exclude = []


class CityForm(forms.Form):
    name = forms.CharField(label='Название', max_length=100)
    parent_city_id = forms.IntegerField(label='Привязка', min_value=1)
    est_time_ufa = forms.DecimalField(label='Время до Уфы', max_digits=4, decimal_places=2)
    est_time_addition = forms.DecimalField(label='Время до привязки', max_digits=4, decimal_places=2)
    dist_ufa = forms.IntegerField(label='Расстояние до Уфы', initial=0, min_value=0, max_value=999)
    dist_parent = forms.IntegerField(label='Расстояние до привязки', initial=0, min_value=0, max_value=99)
    price_addition = forms.IntegerField(label='Добавка к цене', initial=100, min_value=0, max_value=999)

    class Meta:
        model = City
        exclude = []


class RouteForm(forms.Form):
    start_id = forms.IntegerField(label='id начала', min_value=1)
    finish_id = forms.IntegerField(label='id конца', min_value=1)
    price = forms.IntegerField(label='Цена', initial=1000, min_value=100, max_value=9999)

    class Meta:
        model = Driver
        exclude = []
