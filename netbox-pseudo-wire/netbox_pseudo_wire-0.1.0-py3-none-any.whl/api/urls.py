from rest_framework import routers

from .views import PseudowireViewSet


router = routers.DefaultRouter()
router.register("pseudowires", PseudowireViewSet)

urlpatterns = router.urls
