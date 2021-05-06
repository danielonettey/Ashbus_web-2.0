from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from ashbus.ashbus_web.models import *
from django.db.utils import IntegrityError


class BusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus    
        fields = ['seats_occupied', 'status', 'address','location','bus_number']
        read_only_fields = ('route','capacity',)

    def create(self,validated_data):
        try:
            bus = Bus.objects.filter(bus_number=validated_data['bus_number']).first()
            bus.seats_occupied = validated_data['seats_occupied']
            bus.location = validated_data['location']
            bus.status = validated_data['status']
            bus.address = validated_data['address']
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