from django.urls import path
from .views import get_notifications, mark_as_read

urlpatterns = [
    path('', get_notifications, name='get-notifications'),
    path('<int:pk>/read/', mark_as_read, name='mark-as-read'),
]
