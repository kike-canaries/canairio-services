from rest_framework import serializers

from canairio_user.models import CanairioUser

# Create your serializers here.


class CanairioUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    is_active = serializers.BooleanField(source='user.is_active')

    class Meta:
        model = CanairioUser
        fields = ['id', 'username', 'email', 'device_id',
                  'app_version', 'fcm_token', 'is_active']
        depth = 1
