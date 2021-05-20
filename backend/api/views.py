from . import models
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import authModelSerializers
from rest_framework.response import Response

from rest_framework.viewsets import ViewSet
# Create your views here.
class authViews(viewsets.ModelViewSet):
    serializer_class= authModelSerializers
    queryset = models.authModel.objects.all()

    """ 
    def post(self,response, format=None):
        serial = self.serializer_class(data = response.data)
        if serial.is_valid():
            print(serial.data)

        return Response()
    """