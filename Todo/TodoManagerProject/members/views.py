from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import login as auth_login  # Avoid conflict
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
from .forms import UserUpdateForm

# login
def login_user(request):
    if request.method== "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('/home')
            ...
        else:
            messages.success(request, "PLease neter a valid username or password")
            return redirect('/members/login_user')
    else: 
        return render(request,'authenticate/login.html',{})
    

#log out
def logout_user(request):
    logout(request)
    messages.success(request, "You were loged out")
    return redirect('/home')


#register new user
def register_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Avoid using the function name `login`
                messages.success(request, "You have successfully registered.")
                return redirect('/home')
            else:
                messages.error(request, "Authentication failed.")
                return redirect('/members/register')
        else:
            messages.error(request, "Form is not valid. Please correct the errors.")
    
    return render(request, "register.html", {"form": form})



# Update existing user
def Account_info(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('/home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'account.html', {'form': form})

