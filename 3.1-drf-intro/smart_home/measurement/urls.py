from django.urls import path
from measurement.views import ViewSensors, ViewDetailedSensors, ViewMeasurements

urlpatterns = [
    path('sensors/', ViewSensors.as_view()),
    path('sensors/<pk>/', ViewDetailedSensors.as_view()),
    path('measurements/', ViewMeasurements.as_view()),
]
