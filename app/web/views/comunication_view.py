from django.http import HttpResponse
from django.views import View
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from stock.models import StockModel
from comunication.models import ComunicationModel
from clients.models import ClientModel
from django.shortcuts import redirect
from django.urls import reverse

class ComunicationView(LoginRequiredMixin, View):
    def __init__(self, **kwargs) -> None:
        self.template = loader.get_template("web/comunication.html")
        super().__init__(**kwargs)

    def get(self, request):
        stock = StockModel.objects.get(pk=request.GET.get("item"))

        context ={
            "seller": stock.client.pk,
            "initial_text" : f"Hola sr {stock.client.username} queria preguntar acerca del producto: {stock.name} (code:{stock.code}): "
        }
        return HttpResponse(self.template.render(context, request))
    
    def post(self, request):
        ComunicationModel.objects.create(
            client_question = ClientModel.objects.get(pk = int(request.POST.get("client"))),
            client_seller = ClientModel.objects.get(pk = int(request.POST.get("client_seller"))),
            question = request.POST.get("question")
        )
        return redirect(reverse("web:index"))
