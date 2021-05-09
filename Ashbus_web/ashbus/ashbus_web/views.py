from django.shortcuts import render
from ashbus.ashbus_web.models import *
from rest_framework import generics
from rest_framework.response import Response
from ashbus.ashbus_web.serializers import *

# Create your views here.


class BusDataUpdate(generics.CreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusUpdateSerializer 

class TripDataUpdate(generics.CreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripUpdateSerializer

class StaffTripDataUpdate(generics.CreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = StaffTripUpdateSerializer

    

class TripDataCreate(generics.CreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripCreateSerializer

class StaffTripDataCreate(generics.CreateAPIView):
    queryset = Staff_Trip.objects.all()
    serializer_class = StaffTripCreateSerializer


class BusDataGet(generics.ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

class RouteDataGet(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class DriverDataGet(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class StaffDataGet(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class TripDataGet(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class AnnouncementDataGet(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


def HomeView(request):
    route = Route.objects.all()
    trips = Staff_Trip.objects.all()
    one_trip = Trip.objects.all()
    return render(request,"index.html", {"route" : route, "trips" : trips, "one_trip" : one_trip})

def StaffView(request):
    staff = Staff.objects.all()
    return render(request, "staff.html", {"staff":staff})

def DriverView(request):
    driver = Driver.objects.all()
    return render(request, "drivers.html", {"driver":driver})

def BusView(request):
    bus = Bus.objects.all()
    return render(request, "bus.html", {"bus":bus})

def TripView(request):
    trip = Staff_Trip.objects.all()
    one_trip = Trip.objects.all()
    return render(request, "trip.html", {"trips": trip, "one_trip" : one_trip})

def AnnouncementView(request):
    announcement = Announcement.objects.all()
    return render(request, "announcement.html", {"announcement": announcement})


def EditStaffView(request, staff_id):
    staff = Staff.objects.filter(id=staff_id)[0]
    person = Person.objects.filter(id=staff.person.id)[0]

    if request.method == "POST": 
        try:
            person.first_name = request.POST.get('first_name')
            person.last_name = request.POST.get('last_name')
            person.gender = request.POST.get('gender')
            person.email = request.POST.get('email')
            person.gender = "Male"
            person.mobile = request.POST.get('mobile')
            staff.card_id = request.POST.get('card_id')
            staff.amount = request.POST.get('amount')
            person.number_of_trips = request.POST.get('number_of_trips')
            staff.save()
            person.save()
            
            return render(request, 'edit_staff.html', {"staff":staff})
        except Exception :
            raise Exception
        
            return render(request,"Something went wrong")

    else:
        return render(request, 'edit_staff.html', {"staff":staff})

def EditDriverView(request, driver_id):

    driver = Driver.objects.filter(id=driver_id)[0]
    person = Person.objects.filter(id=driver.person.id)[0]
    person = Person.objects.filter(id=driver.person.id)[0]

    if request.method == "POST": 
        try:
            
            person.first_name = request.POST.get('first_name')
            person.last_name = request.POST.get('last_name')
            person.gender = request.POST.get('gender')
            person.email = request.POST.get('email')
            person.gender = "Male"
            person.mobile = request.POST.get('mobile')
            driver.license_number = request.POST.get('card_id')
            driver.ratings = request.POST.get('amount')
            person.number_of_trips = request.POST.get('number_of_trips')
            driver.save()
            person.save()
            
            return render(request, 'edit_driver.html', {"driver":driver})
        except Exception :
            raise Exception
        
            return render(request,"Something went wrong")

    else:
        return render(request, 'edit_driver.html', {"driver":driver})


def EditBusView(request, bus_id):

    bus = Bus.objects.filter(id=bus_id)[0]
    route = Route.objects.filter(id=bus.route.id)[0]

    if request.method == "POST": 
        try:
            bus.bus_number = request.POST.get('bus_number')
            bus.status = request.POST.get('status')
            bus.capacity = request.POST.get('capacity')
            bus.seats_occupied = request.POST.get('seats_occupied')
            route.start_location = request.POST.get('start_location')
            route.end_location = request.POST.get('end_location')
            bus.save()
            route.save()
            
            return render(request, 'edit_bus.html', {"bus":bus})
        except Exception :
            raise Exception
        
            return render(request,"Something went wrong")

    else:
        return render(request, 'edit_bus.html', {"bus":bus})

def EditAnnouncementView(request, announcement_id):

    announcement = Announcement.objects.filter(id=announcement_id)[0]
    if request.method == "POST": 
        try:
            announcement.message = request.POST.get('message')
            announcement.save()            
            return render(request, 'edit_announcement.html', {"announcement":announcement})
        except Exception :
            raise Exception
        
            return render(request,"Something went wrong")

    else:
        return render(request, 'edit_announcement.html', {"announcement":announcement})

        

        