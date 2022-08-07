from django.shortcuts import render
from .models import Vehicle, Reservation
from account.forms import ReservationForm

# Create your views here.


def car(request):
    vehicle_list = Vehicle.objects.all()
    return render(request, 'carshome.html', {'vehicle_list': vehicle_list})


def single(request, slug):
    vehicle = Vehicle.objects.get(slug=slug)
    return render(request, "single.html", {"vehicle": vehicle})


def searchByMake(request):
    make = request.GET.get('make')
    make_list = Vehicle.objects.filter(make=make)
    return render(request, 'carshome.html', {'vehicle_list': make_list})


def searchByModel(request):
    model = request.GET.get('model')
    model_list = Vehicle.objects.filter(mod=model)
    return render(request, 'carshome.html', {'vehicle_list': model_list})


def searchByPrice(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    vehicles_in_range = Vehicle.objects.filter(
        price__gte=min_price, price__lte=max_price)
    return render(request, 'carshome.html', {'vehicle_list': vehicles_in_range})


def reservation(request, slug):
    vehicle = Vehicle.objects.get(slug=slug)
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        reservation_date = request.POST.get('reservation_date')
        return_date = request.POST.get('return_date')
        renter = request.user

        reservation = Reservation.create(
            renter, vehicle, reservation_date, return_date)
        reservation.save()
        return render(request, 'single.html', {'vehicle': vehicle, 'reservation_form': reservation_form})
    reservation_form = ReservationForm()
    return render(request, 'single.html', {'vehicle': vehicle, 'reservation_form': reservation_form})
