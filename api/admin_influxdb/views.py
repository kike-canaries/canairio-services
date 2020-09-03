from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from admin_influxdb.models import AdminInfluxDB
from admin_influxdb.serializers import AdminInfluxDBSerializer

# Create your views here.


class AdminInfluxDBView(APIView):
    """
    Retrieve, create, update or delete an admin_influxdb instance.
    """
    def get(self, request):
        # Get the InfluxDB Admins
        admins_influxdb = AdminInfluxDB.objects.all()
        # AdminInfluxDB Serializer
        serializer = AdminInfluxDBSerializer(admins_influxdb, many=True)
        # Success
        return Response({"status": status.HTTP_200_OK, "message": "Admins InfluxDB", "data": serializer.data}, status=status.HTTP_200_OK)

    # def post(self, request):
    #     # TODO: Something
    #     # return Response(serializer.data, status=status.HTTP_200_OK)

    # def put(self, request):
    #     # TODO: Something
    #     # return Response(serializer.data, status=status.HTTP_200_OK)

    # def delete(self, request):
    #     # TODO: Something
    #     # return Response(serializer.data, status=status.HTTP_200_OK)
