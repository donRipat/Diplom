from .models import *
from django import forms


rcc = 'mt-3'


class CarForm(forms.Form):
    model = forms.CharField(
        label="Цвет, марка, модель",
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
        }),
    )
    plate = forms.CharField(
        label='Регистрационный номер',
        max_length=15,
        widget=forms.TextInput(attrs={
            "class": "form-control",
        }),
    )
    sits = forms.IntegerField(
        label='Количество сидений',
        initial=5,
        max_value=9,
        min_value=2,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
        }),
    )
    required_css_class = rcc

    class Meta:
        model = Car
        exclude = []


class DriverForm(forms.Form):
    name = forms.CharField(
        label='Имя',
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
        }),
    )
    phone = forms.CharField(
        label='Телефон',
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
        }),
    )
    required_css_class = rcc

    class Meta:
        model = Driver
        exclude = []


class CityForm(forms.Form):
    name = forms.CharField(label='Название', max_length=100,
                           widget=forms.TextInput(attrs={"class": "form-control"}))
    area = forms.ModelChoiceField(
        label='Локация',
        widget=forms.Select(attrs={
            "class": "form-control",
        }),
        queryset=Area.objects.all().order_by('name')
    )
    est_time_ufa = forms.DecimalField(
        label='Время до Уфы',
        max_digits=4,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            "class": "form-control"
        }),
    )
    dist_ufa = forms.IntegerField(
        label='Расстояние до Уфы',
        initial=0,
        min_value=0,
        max_value=999,
        widget=forms.NumberInput(attrs={
            "class": "form-control"
        }),
    )
    price_addition = forms.IntegerField(
        label='Добавка к цене',
        initial=100,
        step_size=50,
        min_value=0,
        max_value=999,
        widget=forms.NumberInput(attrs={
            "class": "form-control"
        }),
    )
    required_css_class = rcc

    class Meta:
        model = City
        exclude = []


class RouteForm(forms.Form):
    start_area = forms.ModelChoiceField(
        label='Начало',
        widget=forms.Select(attrs={
            "class": "form-control",
        }),
        queryset=Area.objects.all().order_by('name')
    )
    finish_area = forms.ModelChoiceField(
        label='Конец',
        widget=forms.Select(attrs={
            "class": "form-control",
        }),
        queryset=Area.objects.all().order_by('name')
    )
    price = forms.IntegerField(
        label='Цена',
        initial=1000,
        step_size=50,
        min_value=100,
        max_value=9999,
        widget=forms.NumberInput(attrs={
            "class": "form-control mb-3",
        }),)
    no_reverse_route = forms.BooleanField(
        label='Не добавлять обратный маршрут',
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-inline form-check-input mx-1 mt-1",
        }),
        required=False,
    )
    required_css_class = rcc

    class Meta:
        model = Route
        exclude = []


class AreaForm(forms.Form):
    name = forms.CharField(
        label='Название',
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
        }),
    )
    required_css_class = rcc

    class Meta:
        model = Area
        exclude = []


class RouteChoosingForm(forms.Form):
    route = forms.ModelChoiceField(
        label='Маршрут',
        widget=forms.Select(attrs={
            "class": "form-control",
        }),
        queryset=Route.objects.all().order_by('start_area')
    )
    required_css_class = rcc

    class Meta:
        model = ScheduledRoute
        exclude = []


class TimeAddingForm(forms.Form):
    time = forms.TimeField(
        label='Время',

        widget=forms.TimeInput(attrs={
            "class": "form-control",
            'data-mask': '00:00'
        }),
    )
    required_css_class = rcc

    class Meta:
        model = ScheduledRoute
        exclude = []


class ScheduleForm(forms.Form):
    route = forms.ModelChoiceField(
        label='Маршрут',
        widget=forms.Select(attrs={
            "class": "form-control",
        }),
        queryset=Route.objects.all().order_by('start_area')
    )
    time = forms.TimeField(
        label='Время',

        widget=forms.TimeInput(attrs={
            "class": "form-control",
            # 'type': 'time',
            'data-mask': '00:00'
        }),
    )
    required_css_class = rcc

    class Meta:
        model = ScheduledRoute
        exclude = []
