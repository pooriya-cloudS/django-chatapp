from rest_framework import generics, permissions
from .models import Chat, Message, Membership
from .serializers import ChatSerializer, MessageSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatListCreateView(generics.ListCreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Chat.objects.filter(members=self.request.user)

    def perform_create(self, serializer):
        chat = serializer.save()
        Membership.objects.create(user=self.request.user, chat=chat)


class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        chat_id = self.kwargs.get('chat_id')
        return Message.objects.filter(chat__id=chat_id, chat__members=self.request.user)

    def perform_create(self, serializer):
        chat_id = self.kwargs.get('chat_id')
        serializer.save(
            sender=self.request.user,
            chat=Chat.objects.get(id=chat_id)
        )
