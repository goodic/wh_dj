# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class ViewSensors(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def perform_create(self, serializer):
        return serializer.save(name=self.request.data.get('name'), description=self.request.data.get('description'))


class ViewDetailedSensors(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def perform_update(self, serializer):
        if self.request.data.get('name'):
            serializer.save(name=self.request.data.get('name'))
        if self.request.data.get('description'):
            serializer.save(description=self.request.data.get('description'))


class ViewMeasurements(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        return serializer.save(sensor_id=self.request.data.get('sensor'), temperature=self.request.data.get('temperature'))

