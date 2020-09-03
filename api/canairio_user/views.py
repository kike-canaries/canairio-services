from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User

from django.db.utils import IntegrityError

from canairio_user.models import CanairioUser
from canairio_user.serializers import CanairioUserSerializer

# Create your views here.


class CanairioUserView(APIView):
    """
    Retrieve, create, update or delete a canairio_user instance.
    """
    def get(self, request):
        # Get the Canairio Users
        canairio_users = CanairioUser.objects.all()
        # CanairioUser Serializer
        serializer = CanairioUserSerializer(canairio_users, many=True)
        # Success
        return Response({"status": status.HTTP_200_OK, "message": "Canairio Users", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        # Post new Canairio User
        try:
            user = User(username=request.data.get('username'), password=request.data.get('password'))
            user.save()
        except IntegrityError:
            # Error
            return Response({"status": status.HTTP_409_CONFLICT, "message": "username UNIQUE constraint failed", "data": {}}, status=status.HTTP_409_CONFLICT)
        try:
            canairio_user = CanairioUser(user=user, device_id=request.data.get('device_id'), app_version=request.data.get('app_version'))
            canairio_user.save()
        except IntegrityError:
            # Error
            user.delete()
            return Response({"status": status.HTTP_409_CONFLICT, "message": "device_id UNIQUE constraint failed", "data": {}}, status=status.HTTP_409_CONFLICT)
        # CanairioUser Serializer
        serializer = CanairioUserSerializer(canairio_user)
        # Success
        return Response({"status": status.HTTP_201_CREATED, "message": "Canairio User Registered", "data": serializer.data}, status=status.HTTP_201_CREATED)

    # def put(self, request):
    #     # TODO: Something
    #     # return Response(serializer.data, status=status.HTTP_200_OK)

    # def delete(self, request):
    #     # TODO: Something
    #     # return Response(serializer.data, status=status.HTTP_200_OK)
