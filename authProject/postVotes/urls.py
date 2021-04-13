from .api import PostVotesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/postVotes', PostVotesViewSet, 'postVotes')

urlpatterns = router.urls