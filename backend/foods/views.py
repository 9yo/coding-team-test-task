from django.db.models import Prefetch, Count
from rest_framework import viewsets, mixins

from foods.models import FoodCategory, Food
from foods.serializers import FoodListSerializer


class FoodViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    food_queryset = Food.objects.filter(is_publish=True)

    queryset = FoodCategory.objects.all().prefetch_related(
        Prefetch('food', queryset=food_queryset),
        Prefetch('food__additional', queryset=food_queryset)
        ).annotate(publish_food_qty=Count('food')
        ).filter(publish_food_qty__gt=0).order_by('id')

    serializer_class = FoodListSerializer
