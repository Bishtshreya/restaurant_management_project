from rest_framework import serializers
from .models import Order
from home.models import MenuList  # assuming items come from MenuList


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuList
        fields = ["id", "name", "price"]


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
    model = Order
    fields = ["id", "created_at", "total_amount", "order_status", "order_items"]
