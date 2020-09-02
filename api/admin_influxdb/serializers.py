from rest_framework import serializers

from admin_influxdb.models import AdminInfluxDB

# Create your serializers here.


class AdminInfluxDBSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    is_active = serializers.BooleanField(source='user.is_active')

    class Meta:
        model = AdminInfluxDB
        fields = ['id', 'username', 'influxdb_secret_key',
                  'influxdb_version', 'is_active']
        depth = 1
