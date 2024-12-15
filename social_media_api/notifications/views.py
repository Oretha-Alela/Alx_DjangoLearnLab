from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notifications(request):
    notifications = request.user.notifications.all().order_by('-created_at')
    unread_notifications = notifications.filter(is_read=False)

    data = {
        "unread_count": unread_notifications.count(),
        "notifications": [
            {
                "id": n.id,
                "actor": n.actor.username,
                "verb": n.verb,
                "target": str(n.target),
                "created_at": n.created_at,
                "is_read": n.is_read,
            }
            for n in notifications
        ],
    }
    return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_as_read(request, pk):
    notification = Notification.objects.filter(pk=pk, recipient=request.user).first()
    if not notification:
        return Response({"error": "Notification not found."}, status=status.HTTP_404_NOT_FOUND)

    notification.is_read = True
    notification.save()
    return Response({"message": "Notification marked as read."}, status=status.HTTP_200_OK)
