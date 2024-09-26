from django.urls import path
from . import views

urlpatterns = [
    path('device/<int:device_id>/rdp/', views.rdp_link, name='rdp_link'),
]
