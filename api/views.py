from rest_framework.generics import CreateAPIView

from .serializers import RobotSerializer


class RobotCreateView(CreateAPIView):
    """Представление для создания новых объектов Robot."""
    serializer_class = RobotSerializer
