from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import feeeback_view

urlpatterns = [
    path('contact/', views.contact_us, name="contact"),
    path("menu/", views.menu_items, name="menu"),
    path('about/', views.about_us, name= 'about'),
    path("faq/", views.faq_view, name="faq"),
    path("", views.homepage, name="home"),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path("order/confirmation/", views.order_confirmation, name="order_confirmation"),
    path("feedback/", feedback_view, name="feedback"),
    path("cart/", views.view_cart, name="view_cart"),
    path("cart/add/<int:item_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("thank-you/", views.thank_you, name="thank_you"),
    path("about-chef/", views.about_chef, name = "about_chef")
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path("reservation/", view.reservation, name="reservation"),
    path("our-story/", views.our_story, name="our_story"),
]