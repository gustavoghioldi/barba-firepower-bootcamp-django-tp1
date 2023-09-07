from django.urls import path

from web.views.index_view import IndexView
from web.views.cart_view import CartView
app_name = "web"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('cart/', CartView.as_view(), name="cart"),
]