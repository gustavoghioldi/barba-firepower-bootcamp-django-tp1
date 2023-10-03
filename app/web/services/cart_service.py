from django.db.models import Sum, F
from cart.models import CartModel

class CartService:
    @staticmethod
    def get_context(client):
        cart_context = CartModel.objects.filter(client=client)
        return {
            "cart": cart_context,
            "total": cart_context.aggregate(sum=Sum(F('stock__price')*F('qt')))["sum"]
        }
    
    @staticmethod
    def payout(client):
        cart_context = CartModel.objects.filter(client=client)
        for cart in cart_context:
            cart.delete()