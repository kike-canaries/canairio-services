from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class AdminInfluxDB(models.Model):
    """
    Model to represent the User Admin InfluxDB
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    influxdb_secret_key = models.CharField(max_length=50, unique=True, blank=False)
    influxdb_version = models.CharField(max_length=12, unique=True, blank=False)

    # def __str__(self):
    #     return self.user.username
