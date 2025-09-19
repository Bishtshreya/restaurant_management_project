from django.db import models
from django.contrib.auth.models import User

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

    #  New field for linking to OrderStatus
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    objects = ActiveOrderManager()

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"

class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)  # % or amount
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
        