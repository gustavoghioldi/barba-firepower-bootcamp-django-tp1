from rest_framework import generics
from clients.models import ClientModel
from api.serializers.clients_serializer import ClientsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import  BasicAuthentication
from rest_framework.permissions import BasePermission

class ClientsView(generics.ListCreateAPIView):
    queryset = ClientModel.objects.all()
    serializer_class = ClientsSerializer

class TestView(APIView):
    authentication_classes = [BasicAuthentication]
    def get(self, request, format=None):        
        return Response({"hola":"mundo"})