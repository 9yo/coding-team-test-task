from rest_framework import viewsets, mixins

from foods.models import FoodCategory
from foods.serializers import FoodListSerializer


class FoodViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    queryset = FoodCategory.objects.order_by('id')
    serializer_class = FoodListSerializer
