from django.test import TestCase
from decimal import decimalfrom django.contrib.auth import get_user_model
from .models import Order, OrderItem, Menu, Coupon

User = get_user_model()

class OrderTotalTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="pass")
        self.m1 = Menu.objects.create(name="Item A", price=Decimal("100.00"))
        self.m2 = Menu.objects.create(name="Item B", price=Decimal("50.00"))

    def test_calculate_total_without_coupon(self):
        order = Order.objects.create(customer=self.user)
        OrderItem.objects.create(order=order, menu_item=self.m1, quantity=2, price=self.m1.price)
        OrderItem.objects.create(order=order, menu_item=self.m2, quantity=1, price=self.m2.price)
        self.assertEqual(order.calculate_total(), Decimal("250.00"))

    def test_calculate_total_with_percentage_coupon(self):
        order = Order.objects.create(customer=self.user)
        OrderItem.objects.create(order=order, menu_item=self.m1, quantity=2, price=self.m1.price)
        coupon = Coupon.objects.create(code="PERC10", discount=10, active=True)
        order.coupon = Couponorder.save()
        self.assertEqual(order.total_amount, Decimal("180.00"))  # 200 subtotal with 10% => 180

    def test_calculate_total_with_flat_coupon(self):
        order = Order.objects.create(customer=self.user)
        OrderItem.objects.create(order=order, menu_item=self.m1, quantity=1, price=self.m1.price)
        coupon = Coupon.objects.create(code="FLAT30", discount=30, active=True)
        order.coupon = coupon
        order.save()
        self.assertEqual(order.total_amount, Decimal("70.00"))

