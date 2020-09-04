from django.db import models
from canairio_user.models import CanairioUser

# Create your models here.


class CanairioStation(models.Model):
    """
    Model to represent the Canairio Station
    """
    canairio_user = models.ForeignKey(CanairioUser, on_delete=models.CASCADE)
    mac_address = models.CharField(max_length=24, unique=True, null=False, blank=False)
    firmware_version = models.CharField(max_length=12, null=False, blank=False)
    time_stamp = models.DateTimeField(null=False, blank=False)
    gps_coords = models.CharField(max_length=24, null=False, blank=False)
    country_state_code = models.CharField(max_length=12, null=False, blank=False)
    city_name = models.CharField(max_length=24, null=False, blank=False)
    neighborhood_name = models.CharField(max_length=24, null=False, blank=False)
    zip_code = models.CharField(max_length=12, null=False, blank=False)
    station_id = models.CharField(max_length=12, unique=True, null=False, blank=False)
    used_in = models.CharField(max_length=12, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=True)

    # def __str__(self):
    #     return self.canairio_user.username
