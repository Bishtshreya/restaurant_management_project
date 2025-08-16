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
    restro_name = "Shreya Restro"
    return render(request, 'home/index.html', {'restro_name': restro_name})

def about_us(request):
    restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'Our Restaurant')
    return render(request, 'about.html', {'restaurant_name': restaurant_name})

