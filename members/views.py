from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from members.forms import RegisterUserForm

def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request, ('ERROR'))
            return redirect('login')

    else:
        return render(request,'authenticate/login.html', {})

def logout_user(request):
    messages.success(request, ('You were logged out'))
    logout(request)
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, ('Registration Succesful'))
            return redirect('home')
        else:
            for error in form.errors.items():
                print(error[1][0])
            return render(request, 'authenticate/register_user.html',{'form':form,'errors':form.errors.items()})
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html',{'form':form})