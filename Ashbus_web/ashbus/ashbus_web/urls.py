from django.conf.urls import include,url
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', HomeView, name="index"),
    path('staff/', StaffView, name="staff"),
    path('driver/', DriverView, name="driver"),
    path('bus/', BusView, name="bus"),
    path('trip/', TripView, name="trip"),
    path('editstaff/<int:staff_id>/', EditStaffView, name="edit_staff"),
    path('editdriver/<int:driver_id>/', EditDriverView, name="edit_driver"),
    path('editbus/<int:bus_id>/', EditBusView, name="edit_bus"),
    path('bus_update/', BusDataUpdate.as_view()),
    path('bus_get/', BusDataGet.as_view()),
    path('driver_get/', DriverDataGet.as_view()),
    path('staff_get/', StaffDataGet.as_view()),

]
