from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from .forms import OrederForm
from .models import Order
from customers.models import Customer
from robots.models import Robot


class OrderCreateView(CreateView):
    """Представление для создания нового заказа."""
    model = Order
    form_class = OrederForm
    success_template = 'orders/confirmation.html'

    def post(
            self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponse:
        """Обрабатывает POST-запрос для создания нового заказа."""
        form: OrederForm = self.get_form()
        if form.is_valid():
            robot_serial: str = form.cleaned_data['robot_serial']
            customer, _ = Customer.objects.get_or_create(
                email=form.cleaned_data['email']
            )
            Order.objects.create(
                customer=customer,
                robot_serial=robot_serial
            )
            context = {
                'robot_serial': robot_serial,
                'count_robot': self.get_number_of_robots(robot_serial),
            }
            return render(request, self.success_template, context)
        else:
            self.object = None
            return self.form_invalid(form)

    def get_number_of_robots(self, robot_serial) -> int:
        """Возвращает количество роботов с заданным серийным номером."""
        return Robot.objects.filter(serial=robot_serial).count()
