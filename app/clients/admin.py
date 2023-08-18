from django.contrib import admin
from clients.models import ClientModel

@admin.register(ClientModel)
class ClientAdmin(admin.ModelAdmin):
    pass