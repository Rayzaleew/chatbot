from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from chat.models import Chat


@login_required
def chat_main(request):
    try:
        Chat.objects.filter(user = request.user)[0]
    except:
        chat = Chat(user = request.user)
        chat.save()

    return redirect('chat_id', pk=1)



@login_required
def chat(request, pk):
    return render(request, 'chat/chat.html')



    