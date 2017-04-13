__author__ = 'siddharth'
from app1.views import ProjectViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', ProjectViewSet)
urlpatterns = router.urls
