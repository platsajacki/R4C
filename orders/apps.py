from django.apps import AppConfig
from django.core.signals import setting_changed


class OrdersConfig(AppConfig):
    name = 'orders'

    def ready(self) -> None:
        from .signals import order_waiting_email_signal
        setting_changed.connect(order_waiting_email_signal)
