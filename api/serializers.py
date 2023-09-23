from typing import Any

from rest_framework import serializers

from robots.models import Robot


class RobotSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Robot."""
    created = serializers.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S'])

    class Meta:
        model = Robot
        fields = (
            'serial', 'model',
            'version', 'created'
        )
        read_only_fields = ('serial',)

    def create(self, validated_data: dict[str, Any]) -> Robot:
        """Создает новый объект Robot на основе переданных данных."""
        model = validated_data.get('model')
        version = validated_data.get('version')
        return Robot.objects.create(
            serial=f'{model}-{version}',
            model=model,
            version=version,
            created=validated_data.get('created')
        )
