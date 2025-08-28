from django.contrib import admin
from .models import Feedback
from .models import Menu, Order
from .models import AboutUs

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    search_fields = ('name',)

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

