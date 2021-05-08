from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from ashbus.ashbus_web.models import *
from django.db.utils import IntegrityError


class BusUpdateSerializer(serializers.ModelSerializer):
    route_id = serializers.CharField(write_only=True)

    class Meta:
        model = Bus    
        fields = '__all__'
        # depth = 1
        read_only_fields = ['capacity','route']

    def create(self,validated_data):
        try:
            bus = Bus.objects.filter(bus_number=validated_data['bus_number']).first()
            route_taken = Route.objects.filter(id=validated_data['route_id']).first()
            bus.seats_occupied = validated_data['seats_occupied']
            bus.location = validated_data['location']
            bus.status = validated_data['status']
            bus.address = validated_data['address']
            bus.route = route_taken
            route_taken.save()
            bus.save()
            return bus

        except IntegrityError:
            return ValidationError("Something occured")

# class TripUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Trip    
#         fields = ['driver', 'bus', 'end_time','id']
#         read_only_fields = ['start_time']

#     def create(self,validated_data):
#         try:
            
#             print("\n\n\n\nThis is trip: " + str(validated_data['driver']))
#             print("\n\n\n\nThis is trip: " + str(validated_data['bus']))
#             print("\n\n\n\nThis is trip: " + str(validated_data['id']))
#             print("\n\n\n\nThis is trip: " + str(validated_data['end_time']))
            

#             trip = Trip.objects.filter(id=validated_data['id']).first()

#             print("\n\n\n\nThis is trip: " + str(trip))
#             print("This is trip id from validated data: " + str(validated_data['id']))

#             bus = Bus.objects.filter(bus_number=validated_data['bus']).first()
#             # driver = Driver.objects.filter(id=validated_data['driver']).first()

#             bus.bus_number = "Wow"
#             bus.location = 'location'
#             bus.status = 'status'
#             bus.address = 'address'
#             bus.seats_occupied = 5
#             bus.capacity = 20
#             bus.route.id = 1


#             # staff = Staff.objects.filter(id=staff_id)[0]
#             # person = Person.objects.filter(id=staff.person.id)[0]
#             bus.save()
#             return bus

#         except IntegrityError:
#             return ValidationError("Something occured")


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus    
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route    
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    person = PersonSerializer(read_only=True)
    class Meta:
        model = Driver    
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    person = PersonSerializer(read_only=True)
    class Meta:
        model = Staff    
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    driver = DriverSerializer(read_only=True)
    bus = BusSerializer(read_only=True)
    class Meta:
        model = Trip    
        fields = '__all__'

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        ordering = ("-id")    
        fields = '__all__'



class TripUpdateSerializer(serializers.ModelSerializer):
    trip_id = serializers.CharField(write_only=True)
    bus_location = serializers.CharField(write_only=True)

    class Meta:
        model = Trip    
        fields = '__all__'
        # depth = 1

    def create(self,validated_data):
        try:
            trip = Trip.objects.filter(id=validated_data['trip_id']).first()
            driver_taken = validated_data['driver']
            bus_taken = validated_data['bus']

            trip.start_time = validated_data['start_time']
            trip.end_time = validated_data['end_time']
            trip.driver = validated_data['driver']

            validated_data['bus'].location = validated_data['bus_location']
            validated_data['bus'].save()

            trip.bus = validated_data['bus']
            trip.save()
            return trip

        except IntegrityError:
            return ValidationError("Something occured")