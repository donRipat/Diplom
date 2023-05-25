from .models import *
from django import forms


rcc = 'mt-3'


class CarForm(forms.Form):
    model = forms.CharField(
        label="Цвет, марка, модель",
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            'placeholder': 'Белый Renault Logan',
        }),
    )
    plate = forms.CharField(
        label='Регистрационный номер',
        max_length=15,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            'placeholder': 'X000XX 702 rus',
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
            'placeholder': 'Иванов Иван Иванович',
        }),
    )
    phone = forms.CharField(
        label='Телефон',
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            'data-mask': '+0 (000) 000-00-00',
            'placeholder': '+0 (000) 000-00-00',
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
    est_time_ufa = forms.TimeField(
        label='Время до Уфы',
        widget=forms.TimeInput(attrs={
            "class": "form-control",
            'data-mask': '00:00',
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
    css_class = rcc

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
            'data-mask': '00:00',
            'placeholder': '00:00',
        }),
    )
    required_css_class = rcc

    class Meta:
        model = ScheduledRoute
        exclude = []


class BookingForm(forms.Form):
    client_phone = forms.CharField(
        label='Телефон',
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            'data-mask': '+0 (000) 000-00-00',
            'placeholder': '+0 (000) 000-00-00',
        })
    )
    client_name = forms.CharField(
        label='Имя',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            'placeholder': 'Иванов Иван Иванович',
        }),
    )
    start_city = forms.ModelChoiceField(
        label='Пункт отправления',
        widget=forms.Select(attrs={
            "class": "form-control",
        }),
        queryset=City.objects.all().order_by('name')
    )
    finish_city = forms.ModelChoiceField(
        label='Пункт прибытия',
        widget=forms.Select(attrs={
            "class": "form-control",
        }),
        queryset=City.objects.all().order_by('name')
    )
    date = forms.DateField(
        label='Дата',
        widget=forms.DateInput(attrs={
            "class": "form-control",
            'data-mask': '00.00.0000',
            'placeholder': '01.01.2000',
        }),
    )
    scheduled_route = forms.ModelChoiceField(
        label='Время',
        widget=forms.Select(attrs={
            "class": "form-control",
        }),
        queryset=ScheduledRoute.objects.all(),
    )
    start_address = forms.CharField(
        label='Адрес отправления',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
    )
    finish_address = forms.CharField(
        label='Адрес прибытия',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
    )
    required_css_class = rcc
    css_class = rcc


    class Meta:
        model = Booking
        exclude = []