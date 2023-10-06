from django.db import models
from clients.models import ClientModel
from django.db.models.signals import post_save
from django.dispatch import receiver
from .services.sale_notification_service import SaleNotificationService

class SaleModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    seller = models.ForeignKey(ClientModel, on_delete=models.CASCADE, related_name="sale_model_seller")
    total_amount = models.FloatField()
    #TODO : JSONField
    metadata = models.TextField()

@receiver(post_save, sender=SaleModel)
def hander_post_save(sender, **kwargs):
    sns = SaleNotificationService(kwargs["instance"])
    sns.notification()