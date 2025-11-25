from django.urls import path
from .views import show_orders

urlpatterns = [
    path("orders/", show_orders),
]