from rest_framework import routers, serializers, viewsets
from sigim.models import compbien,contrat

class compbienserializer(serializers.ModelSerializer):
    class Meta:
        model=compbien
        fields='__all__'


class contratserializer(serializers.ModelSerializer):
    class Meta:
        model=contrat
        fields='__all__'