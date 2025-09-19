from django.urls import path
from .views import OrderHistoryView, OrderRetriveView

urlpatterns = [
    path("history/", OrderHistoryView.as_view(), name="order-history"),
    path("<int:pk>/", OrderRetriveView.as_view(), name="order-detail"),
]
    