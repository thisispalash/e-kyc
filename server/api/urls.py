from rest_framework import routers

from .views import DocViewSet, PersonViewSet

router = routers.DefaultRouter()
router.register(r'docs', DocViewSet)
router.register(r'persons', PersonViewSet)

urlpatterns = router.urls