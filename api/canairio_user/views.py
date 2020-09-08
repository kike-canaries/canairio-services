from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from django.contrib.auth.models import User

from django.db.utils import IntegrityError

from canairio_user.models import CanairioUser
from canairio_user.serializers import CanairioUserSerializer

from admin_influxdb.models import AdminInfluxDB

# Create your views here.


class CanairioUserRegisterView(APIView):
    """
    Register a new canairio_user instance.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        # Post new Canairio User
        try:
            # Get the last User
            user = User.objects.last()
            # Create User
            username = 'canario' + str(user.id)
            password = request.data.get('fcm_token')
            email = username + '@example.com'
            user = User(username=username, password=password, email=email)
            # Store the password encripted
            user.set_password(password)
            user.save()
        except IntegrityError as exc:
            # Error
            return Response({"status": status.HTTP_409_CONFLICT, "message": "Canairio User Failed", "data": {"error": str(exc)}}, status=status.HTTP_409_CONFLICT)
        try:
            # Create Canairio User
            canairio_user = CanairioUser(user=user, device_id=request.data.get('device_id'), app_version=request.data.get('app_version'), fcm_token=request.data.get('fcm_token'))
            canairio_user.save()
        except IntegrityError as exc:
            # Error
            user.delete()
            return Response({"status": status.HTTP_409_CONFLICT, "message": "Canairio User Failed", "data": {"error": str(exc)}}, status=status.HTTP_409_CONFLICT)
        # CanairioUser Serializer
        serializer = CanairioUserSerializer(canairio_user)
        # Success
        return Response({"status": status.HTTP_201_CREATED, "message": "Canairio User Registered", "data": serializer.data}, status=status.HTTP_201_CREATED)


class CanairioUserView(APIView):
    """
    Retrieve, create, update or delete a canairio_user instance.
    """
    def get(self, request):
        try:
            # Get the Admin InfluxDB
            AdminInfluxDB.objects.get(user=request.user.id)
        except AdminInfluxDB.DoesNotExist as exc:
            return Response({"status": status.HTTP_401_UNAUTHORIZED, "message": "Canairio Users Failed", "data": {"error": str(exc)}}, status=status.HTTP_401_UNAUTHORIZED)
        # Get the Canairio Users
        canairio_users = CanairioUser.objects.all()
        # CanairioUser Serializer
        serializer = CanairioUserSerializer(canairio_users, many=True)
        # Success
        return Response({"status": status.HTTP_200_OK, "message": "Canairio Users", "data": serializer.data}, status=status.HTTP_200_OK)

    # def post(self, request):
    #     # TODO: Something
    #     # return Response(serializer.data, status=status.HTTP_200_OK)

    # def put(self, request):
    #     # TODO: Something
    #     # return Response(serializer.data, status=status.HTTP_200_OK)

    # def delete(self, request):
    #     # TODO: Something
    #     # return Response(serializer.data, status=status.HTTP_200_OK)
