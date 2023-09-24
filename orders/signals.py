from typing import Any

from django.db.models import QuerySet
from django.db.models.base import ModelBase
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Order
from R4C.utils import send_order_robot_email
from robots.models import Robot


@receiver(pre_save, sender=Robot)
def order_waiting_email_signal(
    sender: ModelBase, instance: Robot, **kwargs: Any
) -> None:
    """
    Сигнальный приемник,
    который отправляет email-сообщение ожидающим покупателям.
    """
    if Robot.objects.filter(serial=instance.serial).count():
        return
    order_list: QuerySet = Order.objects.filter(
        robot_serial=instance.serial
    )
    if order_list.exists():
        recipient_list: list[str] = [
            item[0] for item in set(order_list.values_list('customer__email'))
        ]
        send_order_robot_email(
            recipient_list=recipient_list,
            serial=instance.serial,
            model=instance.model,
            version=instance.version,
            **kwargs
        )
