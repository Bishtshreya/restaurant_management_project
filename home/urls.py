from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_us),
    path('about/', views.about_us, name= 'about'),
    path("faq/", views.faq_view, name="faq"),
    path("", views.homepage_view, name="home"),
]