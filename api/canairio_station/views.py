from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

from canairio_station.models import CanairioStation
from canairio_station.serializers import CanairioStationSerializer

from canairio_user.models import CanairioUser
from canairio_user.serializers import CanairioUserSerializer

from admin_influxdb.models import AdminInfluxDB

import random
import string

# Create your views here.


class CanairioStationView(APIView):
    """
    Retrieve, create, update or delete a canairio_station instance.
    """
    def get(self, request):
        try:
            # Get the Admin InfluxDB
            AdminInfluxDB.objects.get(user=request.user.id)
        except AdminInfluxDB.DoesNotExist as exc:
            return Response({"status": status.HTTP_401_UNAUTHORIZED, "message": "Canairio Stations Failed", "data": {"error": str(exc)}}, status=status.HTTP_401_UNAUTHORIZED)
        # Get the Canairio Stations
        canairio_stations = CanairioStation.objects.all()
        # CanairioStation Serializer
        serializer = CanairioStationSerializer(canairio_stations, many=True)
        # Success
        return Response({"status": status.HTTP_200_OK, "message": "Canairio Stations", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        # Get the Canairio User
        canairio_user = CanairioUser.objects.get(user=request.user.id)
        try:
            # Create random Station ID
            letters_and_digits = (string.ascii_letters + string.digits).lower()
            station_id = 'S' + ''.join((random.choice(letters_and_digits) for i in range(7)))
            # Create Canairio Station
            canairio_station = CanairioStation(
                canairio_user=canairio_user,
                mac_address=request.data.get('mac_address'),
                firmware_version=request.data.get('firmware_version'),
                time_stamp=request.data.get('time_stamp'),
                gps_coords=request.data.get('gps_coords'),
                country_state_code=request.data.get('country_state_code'),
                city_name=request.data.get('city_name'),
                neighborhood_name=request.data.get('neighborhood_name'),
                zip_code=request.data.get('zip_code'),
                station_id=station_id,
                used_in=request.data.get('used_in')
            )
            canairio_station.save()
        except ValidationError as exc:
            # Error
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "Canairio Station Failed", "data": {"error": exc.message}}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as exc:
            # Error
            return Response({"status": status.HTTP_409_CONFLICT, "message": "Canairio Station Failed", "data": {"error": str(exc)}}, status=status.HTTP_409_CONFLICT)
        # CanairioStation Serializer
        serializer = CanairioStationSerializer(canairio_station)
        # Success
        return Response({"status": status.HTTP_201_CREATED, "message": "Canairio Station Registered", "data": serializer.data}, status=status.HTTP_201_CREATED)

    # def put(self, request):
    #     # TODO: Something
    #     # return Response(serializer.data, status=status.HTTP_200_OK)

    # def delete(self, request):
    #     # TODO: Something
    #     # return Response(serializer.data, status=status.HTTP_200_OK)
