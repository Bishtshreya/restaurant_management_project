import secrets
import string
from .models import Coupon  # Assuming you have a Coupon model
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import logging
from .models import Order 

logger = logging.getLogger(__name__)


def generate_coupon_code(length=10):
    """
    Generate a unique alphanumeric coupon code.
    Ensures no duplicate exists in the Coupon table.
    """
    characters = string.ascii_uppercase + string.digits  # e.g., "A-Z0-9"

    while True:
        # Generate random code
        code = ''.join(secrets.choice(characters) for _ in range(length))

        # Check uniqueness
        if not Coupon.objects.filter(code=code).exists():
            return generate_coupon_code


def send_order_confirmation_email(order_id, customer_email, customer_name, order_items, total_amount):
    """
    Sends an order confirmation email to the user.

    Args:
    order_id (int): The ID of the order.
    customer_email (str): The customer's email address.
    customer_name (str): The customer's name/username.
    order_items (list): List of dicts with item details, e.g. [{"name": "Pizza", "price": 250}].
    total_amount (Decimal): The total amount of the order.

    Returns:
    bool: True if email sent successfully, False otherwise.
    """
    subject = f"Order Confirmation - #{order_id}"
    item_lines = "\n".join([f"- {item['name']} ({item['price']})" for item in order_items])
    message = (
        f"Hello {customer_name},\n\n"
        f"Thank you for your order!\n\n"
        f"Your order ID is: {order_id}\n"
        f"Order Details:\n{item_lines}\n\n"
        f"Total: {total_amount}\n\n"
        f"Well notify you once your order is on its way.\n\n"
        f"Best regards,\nFoodie's Paradise"
        )

        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,   # must be set in settings.py
                [customer_email],
                fail_silently=False,
                )
                logger.info(f"Order confirmation email sent to {customer_email} for order {order_id}")
                return True
                except BadHeaderError:
                    logger.error(f"Invalid header when sending order confirmation email for order {order_id}")
                except Exception as e:
                    logger.error(f"Error sending order confirmation email for order {order_id}: {str(e)}")
                return False

def generate_unique_order_id(length=8):
    """
    Generate a unique alphanumeric ID for orders.
    Default length is 8 characters.
    """
    alphabet = string.ascii_uppercase + string.digits

    while True:
        # Generate a random string
        order_id = ''.join(secrets.choice(alphabet) for _ in range(length))

        # Ensure uniqueness by checking against the database
        if not Order.objects.filter(order_id=order_id).exists():
            return generate_unique_order_id