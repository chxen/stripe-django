from rest_framework import routers
from .api import ToDoViewSet

router = routers.DefaultRouter()
router.register('item', ToDoViewSet, 'item')

urlpatterns = router.urls