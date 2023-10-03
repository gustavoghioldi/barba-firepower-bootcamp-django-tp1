from django.db import models
from clients.models import ClientModel


class SaleModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    seller = models.ForeignKey(ClientModel, on_delete=models.CASCADE, related_name="sale_model_seller")
    total_amount = models.FloatField()
    #TODO : JSONField
    metadata = models.TextField()