from django import forms

from .models import Order


class OrederForm(forms.ModelForm):
    """Форма заказа роботов."""
    email = forms.EmailField(required=True)
    robot_serial = forms.CharField(
        required=True,
        help_text=(
            'Введите серийный номер, '
            'объединяя через "-" модель и версию (например R2-D2).'
        )
    )

    class Meta:
        model = Order
        fields = (
            'email',
            'robot_serial'
        )
