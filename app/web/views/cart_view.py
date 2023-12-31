from django.http import HttpResponse
from django.views import View
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.models import CartModel
from stock.models import StockModel
from web.services.cart_service import CartService
from web.forms.checkout_form import CheckoutForm
class CartView(LoginRequiredMixin, View):
    def __init__(self, **kwargs) -> None:
        self.template = loader.get_template("web/cart.html")
        super().__init__(**kwargs)
    
    def get(self, request):
        context = CartService.get_context(request.user)
        if request.GET.get("route") == "checkout":
            self.template = loader.get_template("web/checkout.html")
            context["form"]= CheckoutForm
        
        return HttpResponse(self.template.render(context, request))
    
    def post(self, request):
        #traer stock del producto seleccionado
        stock = StockModel.objects.get(id=request.POST.get("id"))
        
        #trae el item del stock dentro del carro del cliente
        cart_model = CartModel.objects.filter(client=request.user, stock=stock).first()
        #si ya existe el item suma la qt 
        if cart_model:
            cart_model.qt += float(request.POST.get("qt"))
            cart_model.save()
        else:
        #sino crea el item para ese usuario    
            CartModel.objects.create(
                client=request.user, 
                stock=stock, 
                qt=float(request.POST.get("qt")))
        
        #traer el contexto desde un servico
        context = CartService.get_context(request.user)
        return HttpResponse(self.template.render(context, request))