from rest_framework import serializers
from .models import MenuCategory
from .models import MenuList

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ["id", "name"]
class MenuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuList
        fields = ["id", "name", "description", "price", "image", "available"]
        