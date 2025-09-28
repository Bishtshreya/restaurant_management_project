from django.urls import path
from .views import OrderHistoryView, OrderRetriveView, UpdateOrderStatusView

urlpatterns = [
    path("history/", OrderHistoryView.as_view(), name="order-history"),
    path("<int:pk>/", OrderRetriveView.as_view(), name="order-detail"),
    path("update-status/", UpdateOrderStatusView.as_view(), name="update-order-status"),
]
    