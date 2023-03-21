from django.contrib.auth.models import User, Group
from rest_framework.serializers import ModelSerializer
from chat.models import Chat, Message

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class ChatSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'user']
        
class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'message', 'is_user', 'chat']
