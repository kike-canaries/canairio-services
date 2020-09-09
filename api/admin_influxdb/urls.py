# The Django project also has a urls.py file.
# Add a reference to your application's urls.py file.
# Add the URL patterns.

from django.urls import path

from . import views

urlpatterns = [
    path('v1/token-influxdb', views.TokenInfluxDBView.as_view(), name='token-influxdb'),
]
