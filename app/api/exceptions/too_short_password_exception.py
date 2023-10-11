from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_400_BAD_REQUEST

class TooShortPasswordException(APIException):
    def __init__(self):
        super().__init__("password demasiado cortito", HTTP_400_BAD_REQUEST)