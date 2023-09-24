from typing import Any

from django.core.mail import EmailMessage

from constans import TEXT_ORDER_EMAIL


def send_order_robot_email(
        recipient_list: list[str], serial: str,
        model: str, version: str, **kwargs: Any
) -> None:
    """Отправляет email-сообщение о статусе робота."""
    subject: str = f'Статус робота серии {serial}'
    message: str = TEXT_ORDER_EMAIL.format(model=model, version=version)
    from_email: str = 'r4c@r4c.com'
    EmailMessage(
        bcc=recipient_list, subject=subject,
        body=message, from_email=from_email
    ).send()
