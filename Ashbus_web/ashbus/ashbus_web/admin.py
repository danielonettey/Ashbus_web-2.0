from django.contrib import admin
from .models import *
# Register your models here.



admin.site.register([Route,Bus,Person,Staff,Driver,Trip,Staff_Trip,Announcement])