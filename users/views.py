from django.shortcuts import render
from . import models
from .serializers import Userserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
# Create your views here.
class UserView(APIView):
    pass
