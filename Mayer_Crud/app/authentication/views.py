from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer


class AuthenticationView(APIView):
    ## your code here
    ...