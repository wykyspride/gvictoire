from .serializers import compbienserializer,contratserializer
from .models import compbien, client,contrat
from rest_framework import viewsets

class compbienviewset(viewsets.ModelViewSet):
    queryset=compbien.objects.all()
    serializer_class=compbienserializer



class contratviewset(viewsets.ModelViewSet):
    queryset=contrat.objects.all()
    serializer_class=contratserializer
    