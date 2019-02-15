from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from admin_app.forms import *


# Create your views here.

# @login_required
def main(request):

    if not request.user.is_authenticated:

        return redirect('/login')
    else:
        return render(request, 'Admin.html')



def login_view(request):
    if not request.user.is_authenticated:
        form = LoginForm(request.POST or None)
        context = {
            'form': form
        }
        if request.method == 'POST' and form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('/')
        else:
            return render(request, 'login.html', context)
    else:
        return redirect('/')


def registration(request):
    if not request.user.is_authenticated:
        form = RegistrationForm(request.POST or None)
        context = {
            'form': form
        }
        if request.method == 'POST' and form.is_valid():
            username = form.cleaned_data['username']
            user_last_name = form.cleaned_data['user_last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            user.last_name = user_last_name
            user.save()
            return redirect('/')
        else:
            return render(request, 'registration.html', context)
    else:
        return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')
