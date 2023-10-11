from rest_framework import serializers
from clients.models import ClientModel
from django.contrib.auth.hashers import make_password
from api.exceptions.too_short_password_exception import TooShortPasswordException
class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = "__all__"

    def validate(self, attrs):
        if len(attrs["password"]) < 10:
            raise TooShortPasswordException()
        attrs["password"] = make_password(attrs.get("password"))
        return super().validate(attrs)
    