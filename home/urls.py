from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_us),
    path("menu/", views.menu_items, name="menu"),
    path('about/', views.about_us, name= 'about'),
    path("faq/", views.faq_view, name="faq"),
    path("", views.homepage_view, name="home"),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path("order/confirmation/", views.order_confirmation, name="order_confirmation"),
]