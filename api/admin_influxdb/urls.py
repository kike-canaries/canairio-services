# The Django project also has a urls.py file.
# Add a reference to your application's urls.py file.
# Add the URL patterns.

from django.urls import path

from . import views

urlpatterns = [
    path('v1/admin_influxdb', views.AdminInfluxDBView.as_view(), name='admin_influxdb-all'),
]
