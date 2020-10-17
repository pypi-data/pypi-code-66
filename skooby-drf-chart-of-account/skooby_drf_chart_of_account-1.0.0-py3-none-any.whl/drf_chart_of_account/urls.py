"""Chart of Accounts URL Sets."""
from rest_framework.routers import DefaultRouter
from .views import (LayerOneModelViewSet, LayerTwoModelViewSet,
                    LayerThreeModelViewSet, LayerFourModelViewSet,
                    LayerFiveModelViewSet)


router = DefaultRouter()
router.register(r'charts/layer/one', LayerOneModelViewSet, basename='layer_one_viewsets')
router.register(r'charts/layer/two', LayerTwoModelViewSet, basename='layer_two_viewsets')
router.register(r'charts/layer/three', LayerThreeModelViewSet, basename='layer_three_viewsets')
router.register(r'charts/layer/four', LayerFourModelViewSet, basename='layer_four_viewsets')
router.register(r'charts/layer/five', LayerFiveModelViewSet, basename='layer_five_viewsets')
urlpatterns = router.urls
