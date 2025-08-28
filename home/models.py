from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username

class MenuList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="menu_images/", blank=True, null=True)

    def __str__(self):
        return self.name

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

class RestaurantLocation(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, blank=True)
    opening_hours = models.JSONField(default=dict, blank=True)
    logo = models.ImageField(upload_to="restaurant_logos/", blank=True, null=True)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} - {self.zip_code}"

    