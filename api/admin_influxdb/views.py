from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User

from admin_influxdb.models import AdminInfluxDB
from admin_influxdb.serializers import AdminInfluxDBSerializer

import jwt
from datetime import timedelta
from datetime import datetime

# Create your views here.


class TokenInfluxDBView(APIView):
    """
    Retrieve Token InfluxDB
    """
    def get(self, request):
        # Get the InfluxDB Admin
        admin_influxdb = AdminInfluxDB.objects.last()
        # Create InfluxDB Token
        payload = {
            'username': admin_influxdb.user.username,
            "exp": int(datetime.timestamp(datetime.now()) + timedelta(days=1).total_seconds())
        }
        token_influxdb = jwt.encode(payload, admin_influxdb.influxdb_secret_key, algorithm='HS256')
        # Success
        return Response({"status": status.HTTP_200_OK, "message": "Token InfluxDB", "data": {"token_influxdb": token_influxdb}}, status=status.HTTP_200_OK)


class AdminInfluxDBView(APIView):
    """
    Retrieve, create, update or delete an admin_influxdb instance.
    """
    # def get(self, request):
    #     # TODO: Something
    #     # return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request):
    #     # TODO: Something
    #     # return Response(serializer.data, status=status.HTTP_200_OK)

    # def put(self, request):
    #     # TODO: Something
    #     # return Response(serializer.data, status=status.HTTP_200_OK)

    # def delete(self, request):
    #     # TODO: Something
    #     # return Response(serializer.data, status=status.HTTP_200_OK)
