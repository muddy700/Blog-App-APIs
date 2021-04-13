from rest_framework import generics, permissions, viewsets
from .models import PostVote
from .serializers import PostVotesSerializer


class PostVotesViewSet(viewsets.ModelViewSet):
    queryset = PostVote.objects.all()
    permission_classes = [
        permissions.AllowAny,
        # permissions.IsAuthenticated,
    ]
    serializer_class = PostVotesSerializer
