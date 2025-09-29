from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username

#  Menu Category Model
class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Menu Categories"

    def __str__(self):
        return self.name

class MenuList(models.Model):
    category = models.ForeignKey(
        MenuCategory, on_delete=models.CASCADE, related_name="menu_items", null=True, blank=True
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="menu_images/", blank=True, null=True)
    image_alt = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
        
class OpeningHour(models.Model):
    day = models.CharField(max_length=20)  # e.g. Monday
    open_time = models.TimeField()
    close_time = models.TimeField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.day}: {self.open_time.strftime('%I:%M %p')} - {self.close_time.strftime('%I:%M %p')}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(blank=False)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Helpful in admin/list displays
        return f"{self.name}  {self.created_at:%Y-%m-%d %H:%M}"

class AboutUs(models.Model):
    title = models.CharField(max_length=200, default="About Our Restaurant")
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Special(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=True)  # when the special is added

    def __str__(self):
        return self.name
        
class RestaurantInfo(models.Model):
    name = models.CharField(max_length=200, default="Foodie's Paradise")
    phone = models.CharField(max_length=20, default="+91-9876543210")
    email = models.EmailField(default="contact@foodiesparadise.com")
    address = models.TextField(default="123 Main Street, Dehradun, India")

    def __str__(self):
        return self.name

class RestaurantLocation(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, blank=True)
    opening_hours = models.JSONField(default=dict, blank=True)
    logo = models.ImageField(upload_to="restaurant_logos/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} - {self.zip_code}"

class Chef(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to="chef_images/", blank=True, null=True)

    def __str__(self):
        return self.name

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_daily_special = models.BooleanField(default=False)  #  new field

    def __str__(self):
        return self.related_name

class UserReview(models.Model):
    menu_item = models.ForeignKey("Menu", on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()  # e.g., 15
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("menu_item", "user")  # 1 review per user per item

    def __str__(self):
        return f"Review by {self.user.username} on {self.menu_item.name}"