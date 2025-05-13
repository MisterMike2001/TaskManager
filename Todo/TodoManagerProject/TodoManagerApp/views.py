from django.shortcuts import redirect, render, HttpResponse
from .models import Todo
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

# home page 
def home(request):
    if request.user.is_authenticated:
        todos = Todo.objects.filter(userID=request.user)
        counts = {
            'queued': todos.filter(status='queued').count(),
            'in_progress': todos.filter(status='in_progress').count(),
            'completed': todos.filter(status='completed').count(),
            'total': todos.count()
        }
        context = {
            'todos': todos,
            'counts': counts,
        }
        return render(request,"home.html", context)
    else:
        return render(request,"logedoutHome.html")
    


# todo list and items 
def todo_board(request):
    if request.user.is_authenticated:
        todos = Todo.objects.filter(userID=request.user)
        return render(request, 'todo.html', {'todos': todos})
    else:
        return redirect('/members/login_user')

def todo_item(request, ID):
    todoitem = Todo.objects.filter(id=ID).first()
    
    if not todoitem:
        return render(request, "todoitem.html", {"error": "Todo item not found."})
    
    if request.method == 'POST':
        todoitem.title = request.POST.get('title', '')
        todoitem.description = request.POST.get('description', '')
        todoitem.status = request.POST.get('status', '')
        todoitem.save()
        return redirect('todo-board')  # Redirect to the same page after saving
    
    return render(request, "todoitem.html", {"todoitem": todoitem})

def todo_add(request):
    if request.method == 'POST':
        userID = request.user
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        status = request.POST.get('status', '')
        
        new_todo = Todo(userID=userID,title=title, description=description, status=status)
        new_todo.save()
        
        return redirect('todo-board') 
    return render(request, "addTask.html")

def Account(request):
    return render(request,"account.html")

