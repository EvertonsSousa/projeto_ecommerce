from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home_usuario(request):
    return render(request, 'home.html')


def user_logout(request):
    logout(request)
    return redirect('home')