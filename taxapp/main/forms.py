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


areas = Area.objects.all()
area_ch = []
for area in areas:
    area_ch.append((area.id, area.name))
print(area_ch)


class CityForm(forms.Form):
    name = forms.CharField(label='Название', max_length=100,
                           widget=forms.TextInput(attrs={"class": "form-control"}))
    area = forms.ChoiceField(
        label='Локация',
        widget=forms.Select(attrs={
            "class": "form-control",
        }),
        choices=area_ch
    )
    est_time_ufa = forms.DecimalField(label='Время до Уфы', max_digits=4, decimal_places=2,
                                      widget=forms.NumberInput(attrs={"class": "form-control"}))
    dist_ufa = forms.IntegerField(label='Расстояние до Уфы', initial=0, min_value=0, max_value=999,
                                  widget=forms.NumberInput(attrs={"class": "form-control"}))
    price_addition = forms.IntegerField(label='Добавка к цене', initial=100, min_value=0, max_value=999,
                                        widget=forms.NumberInput(attrs={"class": "form-control"}))
    required_css_class = 'mt-3'

    class Meta:
        model = City
        exclude = []


class RouteForm(forms.Form):
    start_area = forms.ChoiceField(
        label='Начало',
        widget=forms.Select(attrs={
            "class": "form-control",
        }),
        choices=area_ch
    )
    finish_area = forms.ChoiceField(
        label='Конец',
        widget=forms.Select(attrs={
            "class": "form-control",
        }),
        choices=area_ch
    )
    price = forms.IntegerField(
        label='Цена',
        initial=1000,
        min_value=100,
        max_value=9999,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
        }),)

    class Meta:
        model = Route
        exclude = []


class AreaForm(forms.Form):
    name = forms.CharField(
        label='Название',
        max_length=50,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
        }),
    )
    required_css_class = 'mt-3'

    class Meta:
        model = Area
        exclude = []
