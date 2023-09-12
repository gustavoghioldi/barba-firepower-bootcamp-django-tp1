from django.http import HttpResponse
from django.views import View
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from comunication.models import ComunicationModel


class ComunicationInteractionView(LoginRequiredMixin, View):
    def __init__(self, **kwargs) -> None:
        self.template = loader.get_template("web/comunication_interaction.html")
        super().__init__(**kwargs)

    def get(self, request):
        comuncations = ComunicationModel.objects.filter(client_question=request.user)
        context ={
            "comuncations" : comuncations
        }
        return HttpResponse(self.template.render(context, request))