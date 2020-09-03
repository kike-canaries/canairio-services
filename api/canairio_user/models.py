from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CanairioUser(models.Model):
    """
    Model to represent the Canairio User
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=50, unique=True, blank=False)
    app_version = models.CharField(max_length=12, blank=False)

    # def __str__(self):
    #     return self.user.username
