from django.contrib import admin
from stock.models import StockModel
@admin.register(StockModel)
class StockAdmin(admin.ModelAdmin):
    pass