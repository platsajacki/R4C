from django.urls import path

from .views import RobotReportTemplateView

app_name = 'robots'

urlpatterns = [
    path('report/', RobotReportTemplateView.as_view(), name='report'),
]
