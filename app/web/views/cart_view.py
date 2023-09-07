from typing import Any
from django.http import HttpResponse
from django.views import View
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from app.settings import IMAGES
from cart.models import CartModel
from stock.models import StockModel
from web.services.cart_service import CartService

class CartView(LoginRequiredMixin, View):
    def __init__(self, **kwargs: Any) -> None:
        self.template = loader.get_template("web/cart.html")
        super().__init__(**kwargs)
    def get(self, request):
        
        context = CartService.get_context(request.user)
        return HttpResponse(self.template.render(context, request))
    
    def post(self, request):
        #traer stock del producto seleccionado
        stock = StockModel.objects.get(id=request.POST.get("id"))
        #comparar si hay la cantidad suficiente del producto selecionado
        if stock.qt < float(request.POST.get("qt")):
            #si no hay la cantidad suficiente lanza exception
            raise Exception("Stock insuficiente")
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
                qt=request.POST.get("qt"))
        #resta del stock
        stock.qt -= float(request.POST.get("qt"))
        stock.save()

        #traer el contexto desde un servico
        context = CartService.get_context(request.user)
        return HttpResponse(self.template.render(context, request))