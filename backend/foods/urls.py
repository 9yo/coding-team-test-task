from rest_framework.routers import DefaultRouter
from .views import FoodViewSet

router = DefaultRouter()
router.register(r'foods', FoodViewSet)
urlpatterns = router.urls
