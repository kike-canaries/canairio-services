from rest_framework import serializers

from canairio_user.models import CanairioUser

# Create your serializers here.


class CanairioUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    is_active = serializers.BooleanField(source='user.is_active')

    class Meta:
        model = CanairioUser
        fields = ['id', 'username', 'device_id',
                  'app_version', 'is_active']
        depth = 1
