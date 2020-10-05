from django.shortcuts import render, redirect
from .forms import CustomUserChangeForm, CustomUserCreationForm
signup login change_password update

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == "POST":
        form = Custom