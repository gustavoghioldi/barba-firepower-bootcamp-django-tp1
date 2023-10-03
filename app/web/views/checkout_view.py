import random
from django.http import HttpResponse
from django.views import View
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from web.forms.checkout_form import CheckoutForm
from sales.services.payment_service import PaymentService
from web.services.cart_service import CartService

class CheckoutView(LoginRequiredMixin, View):
    def __init__(self, **kwargs) -> None:
        self.template = loader.get_template("web/cart.html")
        super().__init__(**kwargs)
    
    def post(self, request):
        form = CheckoutForm(request.POST)
        
        if form.is_valid():
            result = PaymentService.generate_token(form)
            cart = CartService.get_context(request.user)
            payment = PaymentService.pay_transaction(cart.get("total"), str(random.randint(10000000, 999999999999999)), result.json()["id"])

        context = {
            "payment": payment
        }
        if payment:
            CartService.payout(request.user)
            
        template = loader.get_template("web/payment.html")
        
        return HttpResponse(template.render(context, request))