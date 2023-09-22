from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name="home"),
    path('room/',views.room,name="room"),
]

