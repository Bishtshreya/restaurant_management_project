from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 
from .utlis import generate_unique_order_id

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class ActiveOrderManager(models.Manager):
    def get_active_orders(self):
        return self.filter(status__in = ["pending", "processing"])

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(Menu)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Unique, user-friendly alphanumeric order ID
    order_id = models.CharField(max_length=20, unique=True, blank=True)


    #  New field for linking to OrderStatus
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    objects = ActiveOrderManager()
    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = generate_unique_order_id()
        super().save(*args, **kwargs)
    
    def calculate_total(self):
        """Calculate the total order amount based on order items."""
        total = sum(item.subtotal() for item in self.items.all())
        return total

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # copy Menu.price at time of order

    def subtotal(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"

class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)  # % or amount
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
        