from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ChatUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
