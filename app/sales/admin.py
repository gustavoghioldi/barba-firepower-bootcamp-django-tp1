from django.contrib import admin
from .models import SaleModel
# Register your models here.
@admin.register(SaleModel)
class saleModelAdmin(admin.ModelAdmin):
    pass