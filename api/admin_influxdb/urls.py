# The Django project also has a urls.py file.
# Add a reference to your application's urls.py file.
# Add the URL patterns.

from django.urls import path

from . import views

urlpatterns = [
    # Example:
    # path('v1/{app_name}/example', views.{AppName}ExampleView.as_view(), name='{app_name}-example'),
    # ...
]
