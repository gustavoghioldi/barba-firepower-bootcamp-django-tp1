from django.contrib import admin
from .models import CartModel
# Register your models here.
@admin.register(CartModel)
class CartAdmin(admin.ModelAdmin):
    pass