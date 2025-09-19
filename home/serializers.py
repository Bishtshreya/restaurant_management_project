from rest_framework import serializers
from .models import MenuCategory
from .models import MenuList, CustomUser

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ["id", "name"]
class MenuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuList
        fields = ["id", "name", "description", "price", "image", "available"]
        

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email", "phone_number"]
        read_only_fields = ["username", "email"]