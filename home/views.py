from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.shortcuts import render


class MenuAPIView(APIView):
    def get(self, request):
        menu = [
            {"name": "Pasta", "description": "Creamy Alfredo pasta", "price": 250},
            {"name": "Burger", "description": "Beef patty with cheese", "price": 180},
            {"name": "Pizza", "description": "Margherita with fresh basil", "price": 300},
        ]
        return Response(menu)

def homepage(request):
    restro_name = settings.RESTRO_NAME
    phone_number = settings.PHONE_NUMBER
    return render(request, 'home/index.html', {'restro_name': restro_name, 'phone_number': phone_number})

def about_us(request):
    restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'Our Restaurant')
    return render(request, 'home/about.html', {'restaurant_name': restaurant_name})

def contact_us(request):
    return render(request, 'home/contact.html')

def menu_items(request):
    items = [
        {"name": "Margherita Pizza", "price": 299, "description": "Classic cheese pizza with fresh tomato sauce."},
        {"name": "Veg Burger", "price": 199, "description": "Crispy veg patty with lettuce and mayo."},
        {"name": "Pasta Alfredo", "price": 349, "description": "Creamy white sauce pasta with herbs."},
        {"name": "Cold Coffee", "price": 149, "description": "Chilled coffee served with ice cream."},
    ]
    return render(request, "menu.html", {"items": items})

