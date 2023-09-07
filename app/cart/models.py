from django.db import models
from clients.models import ClientModel
from stock.models import StockModel
# Create your models here.
class CartModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    stock = models.ForeignKey(StockModel, on_delete=models.CASCADE)
    qt = models.FloatField()

    class Meta:
        unique_together = ("client", "stock")