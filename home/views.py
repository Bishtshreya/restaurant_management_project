from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.shortcuts import render, redirects, get_objects_or_404
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.utlis import timezone
from .models import MenuList, RestaurantLocation
from .forms import ContactForm
from datetime import datetime
from django.urls import reverse
import random
import .forms import FeedbackForm
import .models import Feedback
from .models import AboutUs
from .models import Special
from .models import OpeningHour
from .forms import Contactform
from .models import restaurantInfo
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
        "year": timezone.now().year,
        "search_results": search_results,
        "query": query,
        "cart_count": total_items_in_cart,
        "current_datetime": timezone.now(),
        "specials": Special.objects.filter(date=date.today())
        "hours: setting.OPENING_HOURS",
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
        #  added cart_count so breadcrumbs/footer match homepage
        cart = request.session.get("cart", {})
        total_items_in_cart = sum(cart.values())

        context = {
                "restaurant_name": restaurant_name,
                "mission": mission,
                "history": history,
                "cart_count": cart_count,
        }
        return render(request, 'about.html', context)
    except Exception as e:
        return JsonResponse({"error": "Failed to load About Us page", "details": str(e)}, status=500)

def about_view(request):
    about = AboutUs.objects.first()  # assuming only 1 entry
    return render(request, "about.html", {"about": about}))

def add_to_cart(request, item_id):
    item = get_object_or_404(MenuList, id=item_id)

    cart = request.session.get('cart', {})

    if str(item_id) in cart:
        cart[str(item_id)]["quantity"] += 1
    else:
        cart[str(item_id)] = {
            "name": item.name,
            "price": float(item.price),  # store as float to be JSON serializable
            "quantity": 1,
        }

        request.session['cart'] = cart_countmessages.success(request, f"{item.name} added to your cart!")
        return redirect('menu')  # redirect back to menu or wherever you like

def view_cart(request):
    cart = request.session.get('cart', {})
    total = sum(item["price"] * item["quantity"] for item in cart.values())
    return render(request, "cart.html", {"cart": cart, "total": total})

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    if str(item_id) in cart:
        del cart[str(item_id)]
        request.session['cart'] = cart_countmessages.success(request, "Item removed from cart.")
    return redirect('view_cart')

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
                return redirect("thank_you")
            except Exception as e:
                messages.error(request, f"Failed to send email: {e}")
    else:       
        form = ContactForm()
    info = restaurantInfo.objects.first()

    return render(request, "contact.html", {"form": form, "info": info})
    
def thank_you(request):
    return render(request, "thank_you.html")

    try:
        #  added cart_count here too
        cart = request.session.get("cart", {})
        total_items_in_cart = sum(cart.values())

        return render(request, 'home/contact.html', {
            "form": form,
            "cart_count": total_items_in_cart,
            "year": timezone.now().year,
            })
    except Exception as e:
        return JsonResponse({"error": "Failed to load Contact Us page", "details": str(e)}, status=500)

def menu_items(request):
    try:
        items = MenuList.objects.all()
        return render(request, "menu.html", {"items": items})
    except Exception as e:
        return JsonResponse({"error": "Failed to load menu items", "details": str(e)}, status=500)

def privacy_policy(request):
    return render(request, 'privacy_policy.html', {
    "year": timezone.now().year
    })

def order_confirmation(request):
    # Generate a dummy order number (in real app this comes from DB)
    order_number = random.randint(10000, 99999)

    cart = request.session.get("cart", {})
    total_items_in_cart = sum(cart.values())

    context = {
        "order_number": order_number,
        "cart_count": total_items_in_cart,
        "year": timezone.now().year,
    }
        return render(request, "order_confirmation.html", context)

def order_page(request):
    # For now just a placeholder page
    return render(request, "orders/order_page.html", {
        "year": timezone.now().year,
        "cart_count": sum(request.session.get("cart", {}).values()),
    })

def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for your feedback!")
            return redirect("feedback")  # redirect to clear POST and show success
    else:
        form = FeedbackForm()

    # Optional: show latest few feedback entries
    recent_feedback = Feedback.objects.order_by("-created_at")[:5]

    return render(request, "feedback.html", {"form": form, "recent_feedback": recent_feedback})

def faq_view(request):
    return render(request, "faq.html", {
        "restaurant_name": "Shreya Restaurant",
        "restaurant_location": {
            "phone_number": "+91-9876543210"
        },
        "year": datetime.now().year,
        "cart_count": sum(request.session.get("cart", {}).values()),
        "current_page": "FAQ"
    })       

