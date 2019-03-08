import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from admin_app.forms import *
from .models import *


# Create your views here.

# @login_required
def main(request):
    if not request.user.is_authenticated:

        return redirect('/login')
    else:
        users = User.objects.all()
        context = {
            'users': users
        }
        return render(request, 'Admin.html', context)


def user_right(request, user_login):
    if not request.user.is_authenticated:

        return redirect('/login')
    else:
        directory = os.getcwd()

        directory = directory.replace('webscis', 'jobs')
        os.chdir(directory)
        files = os.listdir(directory)
        directory = directory.replace('jobs', 'webscis')
        os.chdir(directory)
        user_profile = User.objects.get(username=user_login)
        rights = []
        for project in ProjectRight.objects.all():
            if project.user == user_profile:
                rights.append(project)


        form = GetRightsForm(request.POST or None)
        #rights_form = RightsForm(request.POST)
        context = {
            'user_login': user_login,
            'form': form,
            'files': files,
            #'RightsForm': rights_form,
            'Rights': rights,
        }
        if request.POST and form.is_valid():
            check_admin = form.cleaned_data['is_admin']

            user_per = User.objects.get(username=user_login)
            if check_admin == 'Yes':
                user_per.is_superuser = True
                user_per.save()
            else:
                user_per.is_superuser = False
                user_per.save()
            for right in rights:
                print(right.project)

                right.can_read = request.POST.get('can_read_'+right.project)
                right.can_write = request.POST.get('can_write_' + right.project)
                right.can_exec = request.POST.get('can_exec_' + right.project)
                print(right.can_read, right.can_write, right.can_exec)
                right.save()

            return redirect('/')
        return render(request, 'User_rights.html', context)


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
            directory = os.getcwd()
            directory = directory.replace('webscis', 'jobs')
            os.chdir(directory)
            files = os.listdir(directory)
            directory = directory.replace('jobs', 'webscis')
            os.chdir(directory)
            username = form.cleaned_data['username']
            user_last_name = form.cleaned_data['user_last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            user.last_name = user_last_name
            user.save()
            for file in files:
                project_right = ProjectRight.objects.create(user=user, project=file)
                project_right.save()


            return redirect('/')
        else:
            return render(request, 'registration.html', context)
    else:
        return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')
