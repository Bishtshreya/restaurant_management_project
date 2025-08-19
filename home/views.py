from rest_framework.views import APIView
from rest_framework.response import response
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .models import MenuList

class MenuAPIView(APIView):
    def get(self, request):
        try:
            menu = [
                {"name": "Pasta", "description": "Creamy Alfredo pasta", "price": 250},
                {"name": "Burger", "description": "Beef patty with cheese", "price": 180},
                {"name": "Pizza", "description": "Margherita with fresh basil", "price": 300},
            ]
            return Response(menu, status=200)
        except Exception as e:
            return Response({"error": "Unable to fetch menu", "details": str(e)}, status=500)

def homepage(request):
    try:
        restro_name = getattr(settings, 'RESTRO_NAME', 'Shreya Restro')
        phone_number = getattr(settings, 'PHONE_NUMBER', 'N/A')
        return render(request, 'home/index.html', {
        'restro_name': restro_name,
        'phone_number': phone_number
    })

    except Exception as e:
        return JsonResponse({"error": "Failed to load homepage", "details": str(e)}, status=500)

def about_us(request):
    try:
        restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'Our Restaurant')
        return render(request, 'home/about.html', {'restaurant_name': restaurant_name})
    except Exception as e:
        return JsonResponse({"error": "Failed to load About Us page", "details": str(e)}, status=500)

def contact_us(request):
    try:
        return render(request, 'home/contact.html')
    except Exception as e:
        return JsonResponse({"error": "Failed to load Contact Us page", "details": str(e)}, status=500)

def menu_items(request):
    try:
        items = MenuList.objects.all()
        return render(request, "menu.html", {"items": items})
    except Exception as e:
        return JsonResponse({"error": "Failed to load menu items", "details": str(e)}, status=500)

