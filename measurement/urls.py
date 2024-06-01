from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from measurement.views import SensorView, SensorDetailView, MeasurementView


app_name = "measurements"

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
