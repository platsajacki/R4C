from django.urls import path

from .views import RobotCreateView

urlpatterns = [
    path('v1/create_robot/', RobotCreateView.as_view(), name='create_robot'),
]
