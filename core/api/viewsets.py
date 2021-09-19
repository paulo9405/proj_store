from rest_framework.viewsets import ModelViewSet
from core.api.serializers import StoreSerializer
from core.models import Store
from django_filters.rest_framework import DjangoFilterBackend


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all() #[:15]
    serializer_class = StoreSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('id', 'name')
