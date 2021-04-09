from rest_framework import generics, permissions, viewsets
from .models import Notification
from .serializers import NotificationSerializer


class NotificationsViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = NotificationSerializer

    
class UserNotificationsViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(sender=user.id)

    