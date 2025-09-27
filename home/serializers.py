from rest_framework import serializers
from .models import MenuCategory, Menu
from .models import MenuList, CustomUser
from .models import ContactFormSubmission

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

class ContactFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFormSubmission
        fields = ["id", "name", "email", "message", "submitted_at"]
        read_only_fields = ["id", "submitted_at"]

class DailySpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "name", "price", "is_daily_special"]