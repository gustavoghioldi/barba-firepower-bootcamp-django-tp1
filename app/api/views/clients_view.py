from rest_framework import generics
from clients.models import ClientModel
from api.serializers.clients_serializer import ClientsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from api.permissions.only_staff_can_write import OnlyStaffCanWrite
from api.permissions.api_key import ApiKey
class ClientsView(generics.ListCreateAPIView):
    queryset = ClientModel.objects.all()
    serializer_class = ClientsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [OnlyStaffCanWrite, ApiKey]

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClientModel.objects.all()
    serializer_class = ClientsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [OnlyStaffCanWrite, ApiKey]
class TestView(APIView):
    authentication_classes = [BasicAuthentication]
    def get(self, request, format=None):  
        return Response({"hola":"mundo"})
    
