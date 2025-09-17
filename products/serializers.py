from rest_framework import serializers
from .models import Item
from .models import Menu

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
class MenuSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    
    class Meta:
        model = Menu
        fields = ["id", "name", "price"]

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value

