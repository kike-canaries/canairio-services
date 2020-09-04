from rest_framework import serializers

from canairio_station.models import CanairioStation

# Create your serializers here.


class CanairioStationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CanairioStation
        fields = '__all__'
        # fields = ['id', 'username', 'device_id',
        #           'app_version', 'is_active']
        # depth = 1
