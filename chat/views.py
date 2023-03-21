from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from chat.models import Chat, Message
# from rest_framework import

# Create your views here.
@login_required
def chat_main(request):
    try:
        Chat.objects.filter(user = request.user)[0]
    except:
        chat = Chat(user = request.user)
        chat.save()
    #return render(request, 'chat/chat.html')
    return redirect('chat_id', pk=1)
    #return render(request, 'chat/chat.html')


@login_required
def chat(request, pk):
    # user = User.objects.get(username = request.user.username)
    # chat = Chat.objects.filter(user = user)[pk-1]
    # messages = Message.objects.filter(chat = chat)
    #context = {'messages' : messages}
    #serializer = MessageSerializer(messages, many=True)
    return render(request, 'chat/chat.html')
    #return Response(serializer.data)
    #return HttpResponse(f"You are in {chat.id} chat and you are {user.username}")


    