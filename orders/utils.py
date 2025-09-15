import secrets
import string
from .models import Coupon  # Assuming you have a Coupon model

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