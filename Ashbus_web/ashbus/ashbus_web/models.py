from django.db import models
from datetime import datetime

# Create your models here.
class Route(models.Model):
    start_address = models.CharField(max_length=60,default = "")
    end_address = models.CharField(max_length=60, default = "Ashesi University")
    start_location = models.CharField(max_length=40)
    end_location = models.CharField(max_length=40)
    route = models.TextField(default="w}qa@fwc@DP@zAHPF@ZBAZ@rGClJAzLEhXCpWGfN?fI?rHC~QCvH?xIGdYEbE?rFCx\\EdSCze@GfNAD?~DAlAG?G@MJEBKBa@AqGEkE@mNE_K?cK?gDDiCXoAXuClAyE~Bg@R]DK@]FE?EBCD?@?@CHEHGLmAjAgAnAwCtDiCnDkChDs@p@cGbEq@Z}@n@HTo@Pq@ZQLyApAo@`@s@VgB\\qA`@aDjA}FlBmA\\uAV_E\\yGh@kAFc@@c@Ci@IaBQ{AUgEc@uI}@eFe@uASyDs@uD}@wGoAuFy@eCKmCYeKcA}MsAkMuAuFs@cKaAgHq@mDm@a@I}Bu@iCeAuB_A_I_EyAi@wA]gAOeAGa@Aa@?eANcCZoAPwCTaCBsOw@_DOcJA_AA_AI_AG_Dk@{Bs@}@c@oEkCwBqAeFmDoDeCaDuBkC_BsAq@sCkAgFmByIeDm@]q@i@}EoGaC_DqA{As@k@m@UmBg@kFmAsIoBkD{@gAQkCYcD[oDWcCY}Bg@eBc@aDiAuBo@iDkAWK{@g@g@_@[c@W{@KyBG_@Om@gAoBUa@kA}A[W_Ag@iAm@yAgA{GyEaCeBaAo@cCeBsA_Ao@[wBu@[IA]Cc@[kD@k@Ha@N_@j@w@V[pAeA`BgAv@Uj@GXBtBb@b@LdDfAbDlA`Cz@jAj@TRFJRz@F^z@V")

    
    # For Start Location
    def getStartLat(self):
        return [float(s.strip()) for s in self.start_location.split(",")][0]

    def getStartLng(self):
        return [float(s.strip()) for s in self.start_location.split(",")][1]

    # For End Location
    def getEndLat(self):
        return [float(s.strip()) for s in self.end_location.split(",")][0]

    def getEndLng(self):
        return [float(s.strip()) for s in self.end_location.split(",")][1]

    

    #Generate List of points from encoded points 
    def decode_polyline(self, polyline_str):
        '''Pass a Google Maps encoded polyline string; returns list of lat/lon pairs'''
        ind, lat, lng = 0, 0, 0
        coordinates = []
        changes = {'latitude': 0, 'longitude': 0}

        # Coordinates have variable length when encoded, so just keep
        # track of whether we've hit the end of the string. In each
        # while loop iteration, a single coordinate is decoded.
        while ind < len(polyline_str):
            # Gather lat/lon changes, store them in a dictionary to apply them later
            for unit in ['latitude', 'longitude']: 
                shift, result = 0, 0

                while True:
                    byte = ord(polyline_str[ind]) - 63
                    ind += 1
                    result |= (byte & 0x1f) << shift
                    
                    shift += 5
                    if not byte >= 0x20:
                        break

                if (result & 1):
                    changes[unit] = ~(result >> 1)
                else:
                    changes[unit] = (result >> 1)

            lat += changes['latitude']
            lng += changes['longitude']

            minList = []
            minList.append(lat / 100000.0)
            minList.append(lng / 100000.0)

            coordinates.append(minList)

        return coordinates

    #Convert List Points to floats
    def getRouteList(self):
        return self.decode_polyline(str(self.route).replace("\\\\","\\"))
    
    def __str__(self):
            return str(self.start_address) + " to " + str(self.end_address)


class Bus(models.Model):
    bus_number = models.CharField(max_length=40)
    status = models.CharField(max_length=20)
    capacity = models.IntegerField()
    seats_occupied = models.IntegerField()
    location = models.CharField(max_length=60)
    address = models.CharField(max_length=80)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    def getLat(self):
        return [float(s.strip()) for s in self.location.split(",")][0]

    def getLng(self):
        return [float(s.strip()) for s in self.location.split(",")][1]
        
    def __str__(self):
        return str(self.bus_number)
    
class Person(models.Model):
    email = models.CharField(max_length=40)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    number_of_trips = models.IntegerField(default=0)


    def __str__(self):
        return str(self.first_name)


class Driver(models.Model):
    license_number = models.CharField(max_length=20)
    
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.person.first_name)

class Staff(models.Model):
    card_id = models.CharField(max_length=10)
    amount = models.IntegerField(default=0)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    password = models.CharField(max_length=20, default="")

    def __str__(self):
        return str(self.person.first_name)


class Trip(models.Model):
    cost = models.IntegerField(default=3)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return str(self.start_time)


class Staff_Trip(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=60)
    pickup_Address = models.CharField(max_length=80, default="")
    dropoff_location = models.CharField(max_length=60, default = "5.760627459528241, -0.21990174522088365")
    dropoff_Address = models.CharField(max_length=80, default="Ashesi University ")
    pickup_time = models.TimeField(auto_now=False, auto_now_add=True)
    dropoff_time = models.TimeField(auto_now=False, auto_now_add=False)
    trip_date = models.DateField(auto_now=False,auto_now_add=True)
    payment = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return str(self.trip.start_time) + " - " + str(self.staff.person.first_name) + "  " + str(self.staff.person.last_name) 
    

class Announcement(models.Model):
    message = models.TextField()
    time_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.message)