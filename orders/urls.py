from django.urls import path
from .views import OrderHistoryView, OrderRetriveView, OrderCancelView

urlpatterns = [
    path("history/", OrderHistoryView.as_view(), name="order-history"),
    path("<int:pk>/", OrderRetriveView.as_view(), name="order-detail"),
    path("orders/cancel/<int:pk>/", OrderCancelView.as_view, name="order-cancel")
]
    