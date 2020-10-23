from django.urls import path
from rest_framework import routers

from .views import MemberViewSet

router = routers.DefaultRouter()
router.register('members', MemberViewSet)

urlpatterns = router.urls
