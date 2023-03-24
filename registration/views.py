from django.shortcuts import render, redirect
from .forms import ChatUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('chat')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('chat')
        else:
            messages.error(request, 'Username OR password does not exit')

    return render(request, 'registration/login.html')

def registerPage(request):
    form = ChatUserCreationForm()

    if request.method == 'POST':
        form = ChatUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('chat')

        else:
            messages.error(request, 'Form is not valid')

    return render(request, 'registration/registration.html', {'form': form})