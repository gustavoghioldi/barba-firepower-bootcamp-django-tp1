from django.http import HttpResponse
from django.views import View
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from web.forms.checkout_form import CheckoutForm
from sales.services.payment_service import PaymentService
class CheckoutView(LoginRequiredMixin, View):
    def __init__(self, **kwargs) -> None:
        self.template = loader.get_template("web/cart.html")
        super().__init__(**kwargs)
    
    def post(self, request):
        form = CheckoutForm(request.POST)
        if form.is_valid():
            result = PaymentService.generate_token(form)
            payment = PaymentService.pay_transaction(2000, "2229999", result.json()["id"])
        context = {}
        
        return HttpResponse(self.template.render(context, request))