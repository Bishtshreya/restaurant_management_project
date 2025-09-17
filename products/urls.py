from django.urls import path, include
from .views import MenuViewSet
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'menu', MenuViewSet, basename="menu")

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path("", include(router.urls)),
]