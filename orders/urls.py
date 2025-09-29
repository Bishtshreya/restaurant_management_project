from django.urls import path
from .views import  get_order_status, OrderHistoryView, OrderRetriveView, UpdateOrderStatusView

urlpatterns = [
    path("history/", OrderHistoryView.as_view(), name="order-history"),
    path("<int:pk>/", OrderRetriveView.as_view(), name="order-detail"),
    path("<int:order_id>/update-status/", UpdateOrderStatusView.as_view(), name="update-order-status"),
    path("<int:order_id>/status/", get_order_status, name="order-status"),
]
    