from sales.models import SaleModel
from django.core import serializers

class PayoutService:
    @staticmethod
    def post_payout(cart):
        SaleModel.objects.create(
            client=cart.client,
            seller = cart.stock.client,
            total_amount = cart.qt * cart.stock.price,
            metadata = serializers.serialize('json', [cart])
        )