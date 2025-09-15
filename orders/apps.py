from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError

class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'

    def ready(self):
        from .models import OrderStatus
        from . import ORDER_STATUS_CHOICES
        try:
            for status in ORDER_STATUS_CHOICES:
                OrderStatus.objects.get_or_create(name=status)
        except (OperationalError, ProgrammingError):
            # Database not ready during first migrate
            pass
