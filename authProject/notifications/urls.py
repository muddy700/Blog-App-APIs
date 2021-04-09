from .api import NotificationsViewSet, UserNotificationsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/notifications', NotificationsViewSet, 'notifications')
router.register('api/user/notifications', UserNotificationsViewSet, 'user-notifications')

urlpatterns = router.urls