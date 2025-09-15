from django.contrib import admin
from .models import RestaurantInfo, Chef, OpeningHour, MenuList, Order, Feedback, MenuCategory

@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(MenuList)
class MenuListAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "available", "category")
    list_filter = ("available", "category")
    search_fields = ("name", "description")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'quantity', 'ordered_at')
    list_filter = ('ordered_at',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name", "message")
    ordering = ("-created_at",)

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(OpeningHour)
class OpeningHourAdmin(admin.ModelAdmin):
    list_display = ("day", "open_time", "close_time")
    ordering = ("id",)

@admin.register(RestaurantInfo)
class RestaurantInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "address")

@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ("name")