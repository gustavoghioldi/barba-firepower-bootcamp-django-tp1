from django.db import models
from django.contrib.auth.models import AbstractUser

class BusinessLineChoices(models.TextChoices):
    FERRETERIA = "Ferreteria"
    ALMACEN    = "Almacen"
    OTROS      = "Otros"

class ClientModel(AbstractUser):
    cuit = models.CharField(max_length=11)
    business_line = models.CharField(choices=BusinessLineChoices.choices, max_length=128, default=BusinessLineChoices.OTROS.value)
    business_line_interes = models.CharField(choices=BusinessLineChoices.choices, max_length=128, default=BusinessLineChoices.OTROS.value)
    is_seller = models.BooleanField(default=False)
    is_buyer  = models.BooleanField(default=True)
    state = models.CharField(max_length=128)
    city  = models.CharField(max_length=128)
    postal_code = models.CharField(max_length=4)
    phone_number = models.CharField(max_length=64)
