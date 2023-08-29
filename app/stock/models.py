from django.db import models
from clients.models import ClientModel, BusinessLineChoices
class StockModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    business_line = models.CharField(choices=BusinessLineChoices.choices, max_length=128, default=BusinessLineChoices.OTROS.value)
    qt = models.FloatField(default=0)
    price = models.FloatField(default=0)
    name = models.CharField(max_length=128)
    description = models.TextField()
    code = models.CharField(max_length=32)
    expiration = models.DateField(null=True, default=None)
    class Meta:
        unique_together = ("client", "code")