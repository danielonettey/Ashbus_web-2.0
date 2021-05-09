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
        read_only_fields = ['capacity','route','capacity','address','seats_occupied','location']

    def create(self,validated_data):
        try:
            bus = Bus.objects.filter(bus_number=validated_data['bus_number']).first()
            route_taken = Route.objects.filter(id=validated_data['route_id']).first()
            # bus.seats_occupied = validated_data['seats_occupied']
            # bus.location = validated_data['location']
            bus.status = validated_data['status']
            # bus.address = validated_data['address']
            bus.route = route_taken
            route_taken.save()
            bus.save()
            return bus

        except IntegrityError:
            return ValidationError("Something occured")


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



class TripCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip    
        fields = '__all__'

class StaffTripCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff_Trip    
        fields = '__all__'




class StaffTripUpdateSerializer(serializers.ModelSerializer):
    trip_id = serializers.CharField(write_only=True)
    class Meta:
        model = Staff_Trip    
        fields = ['trip_id','dropoff_location','dropoff_Address','dropoff_time','payment']

    def create(self,validated_data):
        try:
            staff_Trip = Staff_Trip.objects.filter(id=validated_data['trip_id']).first()
            staff_Trip.dropoff_location = validated_data['dropoff_location']
            staff_Trip.dropoff_Address = validated_data['dropoff_Address']
            staff_Trip.dropoff_time = validated_data['dropoff_time']
            staff_Trip.payment = validated_data['payment']
            staff_Trip.save()
            return staff_Trip

        except IntegrityError:
            return ValidationError("Something occured")


class TripUpdateSerializer(serializers.ModelSerializer):
    trip_id = serializers.CharField(write_only=True)
    bus_location = serializers.CharField(write_only=True)
    bus_status = serializers.CharField(write_only=True)
    bus_address = serializers.CharField(write_only=True)

    class Meta:
        model = Trip    
        fields = '__all__'
        read_only_fields = ['start_time']
        # depth = 1

    def create(self,validated_data):
        try:
            trip = Trip.objects.filter(id=validated_data['trip_id']).first()
            driver_taken = validated_data['driver']
            bus_taken = validated_data['bus']

            # trip.start_time = validated_data['start_time']
            trip.end_time = validated_data['end_time']
            trip.driver = validated_data['driver']

            validated_data['bus'].location = validated_data['bus_location']
            validated_data['bus'].status = validated_data['bus_status']
            validated_data['bus'].address = validated_data['bus_address']


            validated_data['bus'].save()

            trip.bus = validated_data['bus']
            trip.save()
            return trip

        except IntegrityError:
            return ValidationError("Something occured")