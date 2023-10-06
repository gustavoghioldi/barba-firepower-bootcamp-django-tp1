from rest_framework import serializers
from clients.models import ClientModel

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = "__all__"