from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib import messages
from .models import MenuList, RestaurantLocation
from .forms import ContactForm
from datetime import datetime


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
    
    #basic search functionality
    query = request.GET.get("q")
    search_results = None
    if query:
        search_results = MenuList.objects.filter(name__icontains=query)
    # get cart from session 
    cart =  request.session.get("cart", {})
    total_items_in_cart = sum(cart.values()) 
    
    context = {
        "restaurant_name": "Shreya Restaurant",
        "phone_number": restaurant_location.phone_number if restaurant_location else getattr(settings, "PHONE_NUMBER", "N/A"),
        "restaurant_location": restaurant_location,
        "year": timezone.now(.year),
        "search_results": search_results,
        "query": query,
        "cart_count": total_items_in_cart,
        "current_datetime": timezone.now(),
    }
    return render(request, "index.html", context)
    
def about_us(request):
    try:
        restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'Our Restaurant')
        mission = "To serve delicious food made from the freshest ingredients while offering warm hospitality."
        history = (
            f"{restaurant_name} started as a small family-run business with a love for food and community. "
            "Over the years, it has grown into a favorite local spot where people come to relax and enjoy quality meals."
        )
        context = {
                "restaurant_name": restaurant_name,
                "mission": mission,
                "history": history,
                "cart_count": cart_count,
        }
        return render(request, 'about.html', context)
    except Exception as e:
        return JsonResponse({"error": "Failed to load About Us page", "details": str(e)}, status=500)

def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            subject = f"New Contact Message from {contact.name}"
            message = f"Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.CONTACT_EMAIL]  # configure in settings.py

            try:
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                messages.success(request, "Your message has been sent successfully!")
            except Exception as e:
                messages.error(request, f"Failed to send email: {e}")

    else:       
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

def privacy_policy(request):
    return render(request, 'privacy_policy.html')
        
def faq_view(request):
    return render(request, "faq.html", {
        "restaurant_name": "Shreya Restaurant",
        "restaurant_location": {
            "phone_number": "+91-9876543210"
        },
        "year": datetime.now().year,
        "current_page": "FAQ"
    })       

