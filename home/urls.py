from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from . import views
from .views import feeeback_view, TableDetailView, AvailableTablesAPIView, RestaurantInfoAPIView
from .views import MenuCategoryListView, MenuCategoryViewSet ContactFormSubmissionView, UpdateMenuItemAvailabilityAPIView
from .views import MenuSearchAPIView, UserProfileUpdateView, DailySpecialsView, UserReviewCreateView, UserReviewListView

router = DefaultRouter()
router.register(r'menu-categories', MenuCategoryViewSet, basename='menu-category')

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
    path("reservations/", view.reservations, name="reservations"),
    path("our-story/", views.our_story, name="our_story"),
    path("team/", views.team, name="team"),
    path("privacy/", views.privacy, name="privacy"),
    path("gallery/", views.gallery, name="gallery"),
    path("locations/", views.locations, name="locations"),
    path("api/menu-categories/", MenuCategoryListView.as_view(), name="menu-categories"),
    path("api/menu/search/", MenuSearchAPIView.as_view(), name="menu-search"),
    path("profile/", UserProfileUpdateView.as_view(), name ="user-profile-update"),
    path("api/contact/", ContactFormSubmissionView.as_view(), name="contact-form"),
    path("daily-specials/", DailySpecialsView.as_view(), name="daily-specials"),
    path("reviews/create/", UserReviewCreateView.as_view(), name="create-review"),
    path("reviews/<int:menu_item_id>/", UserReviewListView.as_view(), name="menu-item-reviews"),
    path('', include(router.urls)),
    path('tables/<int:pk>/', TableDetailView.as_view(), name='table-detail'),
    path('api/tables/available/', AvailableTablesAPIView.as_view(), name='available_tables_api'),
    path('api/restaurant/info/', RestaurantInfoAPIView.as_view(), name='restaurant_info'),
    path('api/menu/<int:pk>/availability/', UpdateMenuItemAvailabilityAPIView.as_view(), name='update_menu_availability'),
]