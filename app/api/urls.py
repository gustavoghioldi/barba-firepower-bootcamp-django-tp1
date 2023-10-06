from django.urls import path
from api.views.clients_view import ClientsView, TestView

urlpatterns = [
    path('clients/', ClientsView.as_view()),
    path('test/', TestView.as_view()),
]