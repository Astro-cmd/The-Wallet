from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.core.exceptions import ValidationError
from . serializers import BudegetSerialzer
from . models import Budgets

# Create your views here.
class BudgetAPiView(APIView):
    def get(self, request):
        queryset = Budgets.objects.all()
        serializer = BudegetSerialzer(queryset, many = True)
        data = {
            'message': 'succescfully got all the budgets',
            'result' : serializer.data
        }
        return Response(data, status = status.HTTP_200_OK)
    
    def post(self, request):
        "first retrieve all the data from the serializer"
        serializer = BudegetSerialzer(data = request.data)
        input_data = request.data

        " create new budget objects"
        new_budget = Budgets.objects.create(**input_data)

        "error handling before adding new objects"
        try:
            # check if the data is valid 
            serializer.is_valid(raise_exception=True)

            serializer.save()
            return Response({
                'message' : 'new budget added succesfully',
                'result' : serializer.data
            }, status= status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({
                'message' : 'An was raised while adding budget',
                'errors' : str(e)
            }, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
        