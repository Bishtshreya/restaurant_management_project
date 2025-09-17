from django.urls import path, include
from .views import MenuViewSet
from rest_framework.routers import DefaultRouter
from .views import *
from .views import MenuByCategoryAPIView

router = DefaultRouter()
router.register(r'menu', MenuViewSet, basename="menu")

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path("", include(router.urls)),
    path("menu/by-category/", MenuByCategoryAPIView.as_view(), name="menu-by-category"),
]