from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home_usuario(request):
    pass


def user_logout(request):
    logout(request)
    return redirect('home')