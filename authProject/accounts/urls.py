from .api import UsersViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/users', UsersViewSet, 'users')

urlpatterns = router.urls