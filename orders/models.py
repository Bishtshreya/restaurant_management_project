from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 
from decimal import decimal 
from django.utils import timezone
from .utils import calcultae_discount_for_order
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

class OrderManager(models.Manager):
    def with_status(self, status_name):
        """Return orders filtered by a given status name (case-insensitive)."""
        return self.filter(status__name__iexact=status_name)

    def pending(self):
        """Shortcut for pending orders."""
        return self.with_status("pending")

    def processing(self):
        """Shortcut for processing orders."""
        return self.with_status("processing")

    def completed(self):
        """Shortcut for completed orders."""
        return self.with_status("completed")


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(Menu)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Unique, user-friendly alphanumeric order ID
    order_id = models.CharField(max_length=20, unique=True, blank=True)

    # New optional coupon field  add migrations if you include this
    coupon = models.ForeignKey("Coupon", null=True, blank=True, on_delete=models.SET_NULL, related_name="orders")

    #  New field for linking to OrderStatus
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    objects = ActiveOrderManager()

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = generate_unique_order_id()
        
        self.total_amount = self.calculate_total()
        super().save(*args, **kwargs)
    
    def calculate_total(self) -> Decimal:
        """
        Calculate total cost of the order:
        - Sum (price * quantity) across OrderItem instances related to this order
        - Apply discount (via calculate_discount_for_order) if applicable
        - Return Decimal total (>= 0)
        """
        subtotal = Decimal("0.00")
        # `items` is the related_name on OrderItem in our previous examples
        for oi in self.items.all():            # OrderItem has related_name="items"
            price = Decimal(str(oi.price or 0))
            qty = int(oi.quantity or 0)
            subtotal += (price * qty)

        # Compute discount amount (safe; function returns Decimal)
        discount_amount = calculate_discount_for_order(self, subtotal)

        total = subtotal - discount_amount
        if total < Decimal("0.00"):
            total = Decimal("0.00")
        # Round to two decimals
        return total.quantize(Decimal("0.01"))  

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
    is_active = models.BooleanField(default=True)
    valid_from = models.DateField()
    valid_until = models.DateField()

    def __str__(self):
        return f"{self.code} ({self.discount_percentage}% off)"

    def is_valid(self):
        """Check if coupon is active and within validity period"""
        today = timezone.now().date()
        return self.is_active and self.valid_from <= today <= self.valid_until
        