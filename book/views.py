from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.contrib.auth.models import User
class UserView(APIView):
    def get(self, request, id: int):
        try:
            user = User.objects.get(id=id)
            return Response({"username": user.username, "first_name": user.first_name, "last_name": user.first_name})
        except:
            return Response({'result': 'The User you searched for was not found'})
class Users(APIView):
    def get(self, request):
        try:
            data = []
            users = User.objects.all()
            for user in users:
                data.append({"username": user.username,
                            "first_name": user.first_name, "last_name": user.first_name})
            return Response(data)
        except:
            return Response({'result': 'Users not found'})
# Create your views here.
