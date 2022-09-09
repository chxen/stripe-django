from .models import Item
from rest_framework import viewsets, permissions

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
