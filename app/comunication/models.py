from django.db import models
from clients.models import ClientModel
# Create your models here.
class ComunicationModel(models.Model):
    client_question = models.ForeignKey(ClientModel, on_delete=models.DO_NOTHING, related_name="client_question")
    client_seller = models.ForeignKey(ClientModel,on_delete=models.CASCADE, related_name="client_seller")
    question = models.TextField()
    answer = models.TextField(blank=True, default="")

    @property
    def is_answer(self):
        return bool(self.answer)
