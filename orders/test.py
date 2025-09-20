from django.test import TestCase
from django.contrib.auth.models import User
from decimal import decimalfrom .models import Order, OrderItem, MenuItem, OrderStatus

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.status = OrderStatus.objects.create(name="pending")
        self.menu1 = MenuItem.objects.create(name="Burger", price=100)
        self.menu2 = MenuItem.objects.create(name="Fries", price=50)

        self.order = Order.objects.create(customer=self.user, status=self.status)

        OrderItem.objects.create(order=self.order, menu_item=self.menu1, quantity=2, price=self.menu1.price)
        OrderItem.objects.create(order=self.order, menu_item=self.menu2, quantity=3, price=self.menu2.price)

    def test_calculate_total(self):
        total = self.order.calculate_total()
        self.assertEqual(total, Decimal("350.00"))  # 2*100 + 3*50
