from .api import PostViewSet, UserPostsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/posts', PostViewSet, 'posts')
router.register('api/user/posts', UserPostsViewSet, 'user-posts')

urlpatterns = router.urls