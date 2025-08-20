from rest_framework.views import APIView
from rest_framework.response import response
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .models import MenuList
from .forms import ContactForm
from .models import Restaurantlocation

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
    restaurant_location = RestaurantLocation.objects.first()  # Get first location (assuming only one)
    context = {
        "restaurant_name": "Shreya Restaurant",
        "phone_number": "+91 9876543210",
        "restaurant_location": restaurant_location,
        "year": 2025
    }
    return render(request, "home.html", context)
    
def about_us(request):
    try:
        restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'Our Restaurant')
        return render(request, 'home/about.html', {'restaurant_name': restaurant_name})
    except Exception as e:
        return JsonResponse({"error": "Failed to load About Us page", "details": str(e)}, status=500)

def contact_us(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    form = ContactForm()
    
    try:
        return render(request, 'home/contact.html', {"form": form})
    except Exception as e:
        return JsonResponse({"error": "Failed to load Contact Us page", "details": str(e)}, status=500)

def menu_items(request):
    try:
        items = MenuList.objects.all()
        return render(request, "menu.html", {"items": items})
    except Exception as e:
        return JsonResponse({"error": "Failed to load menu items", "details": str(e)}, status=500)

