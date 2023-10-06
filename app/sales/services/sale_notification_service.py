from comunication.models import ComunicationModel
from stock.models import StockModel
import json

class SaleNotificationService:
    def __init__(self, instance):
        self.instance = instance

    def notification(self):
        com = ComunicationModel()
        com.client_question = self.instance.client
        com.client_seller= self.instance.seller
        instance_metadata = json.loads(self.instance.metadata)[0]
        stock_name = StockModel.objects.get(pk=instance_metadata.get("fields").get("stock")).name
        qt = instance_metadata.get("fields").get("qt")
        total = self.instance.total_amount
        com.question = f"Compra articulo: {stock_name} - qt {qt} - total: {total}"
        com.save()