from django.db import models
from clients.models import ClientModel
from stock.models import StockModel
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from stock.service import StockService
from django_q.tasks import async_task
from sales.services.cart_payout_service import PayoutService
# Create your models here.
class CartModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    stock = models.ForeignKey(StockModel, on_delete=models.CASCADE)
    qt = models.FloatField()

    class Meta:
        unique_together = ("client", "stock")

@receiver(pre_save, sender=CartModel)
def hander_pre_save(sender, **kwargs):
    #comparar si hay la cantidad suficiente del producto selecionado
    if kwargs["instance"].stock.qt < kwargs["instance"].qt:
            #si no hay la cantidad suficiente lanza exception
            raise Exception("Stock insuficiente")
    if kwargs["instance"].pk:
        qt = kwargs["instance"].qt - CartModel.objects.get(pk=kwargs["instance"].pk).qt
    else:
        qt = kwargs["instance"].qt
    async_task(StockService.sock_managment_down, kwargs["instance"].stock, qt)

@receiver(post_delete, sender=CartModel)
def hander_post_delete(sender, **kwargs):
    PayoutService.post_payout(kwargs["instance"])
