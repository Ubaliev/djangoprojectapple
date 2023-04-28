from rest_framework.viewsets import ModelViewSet

from mainapp.models import (
    Iphone, Macbook, Airpods,
)

from mainapp.serializers import(
    IphoneSerializer, MacbookSerializer, AirpodsSerializer,
)

class IphoneView(ModelViewSet):
    queryset = Iphone.objects.all()
    serializer_class = IphoneSerializer

class MacbookView(ModelViewSet):
    queryset = Macbook.objects.all()
    serializer_class = MacbookSerializer

class AirpodsView(ModelViewSet):
    queryset = Airpods.objects.all()
    serializer_class = AirpodsSerializer