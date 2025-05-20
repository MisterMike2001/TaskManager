from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import Todo, UserTeams, Team, Notification
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





#Personal board
def todo_item(request, ID):
    todoitem = Todo.objects.filter(id=ID).first()
    # Get list of team IDs the user belongs to
    user_team_ids = UserTeams.objects.filter(user=request.user).values_list('team_id', flat=True)
    
    # Fetch Team objects for display
    teams = Team.objects.filter(id__in=user_team_ids)
    
    if not todoitem:
        return render(request, "todoitem.html", {"error": "Todo item not found."})
    
    if request.method == 'POST':
        todoitem.title = request.POST.get('title', '')
        todoitem.description = request.POST.get('description', '')
        todoitem.status = request.POST.get('status', '')
        team_id = request.POST.get('team')

        if team_id:
            try:
                todoitem.teamID = Team.objects.get(id=team_id)
            except Team.DoesNotExist:
                todoitem.teamID = None
        else:
            todoitem.teamID = None

        todoitem.save()
        return redirect('todo-board')# Redirect to the same page after saving
    
    return render(request, "todoitem.html", {"todoitem": todoitem, "teams": teams})






def todo_add(request):
    # Get list of team IDs the user belongs to
    user_team_ids = UserTeams.objects.filter(user=request.user).values_list('team_id', flat=True)
    
    # Fetch Team objects for display
    teams = Team.objects.filter(id__in=user_team_ids)

    if request.method == 'POST':
        userID = request.user
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        status = request.POST.get('status', '')
        team_id = request.POST.get('team')

        new_todo = Todo(
            userID=userID,
            title=title,
            description=description,
            status=status,
            teamID_id=team_id if team_id else None  # safe fallback
        )
        new_todo.save()

        return redirect('todo-board')

    return render(request, "addTask.html", {"teams": teams})





#team 
def team_board(request, teamid):
    if not request.user.is_authenticated:
        return redirect('/members/login_user')

    user_team_ids = UserTeams.objects.filter(user=request.user).values_list('team_id', flat=True)
    teams = Team.objects.filter(id__in=user_team_ids)

    # Check if the user has access to the requested team
    if teamid:
        if teamid not in user_team_ids:
            return render(request, "teamboard.html", {"error": "Access denied.", "teams": teams})

        todos = Todo.objects.filter(teamID_id=teamid)
    else:
        teamid = user_team_ids.first()
        todos = Todo.objects.filter(teamID_id=teamid)

    return render(request, 'teamboard.html', {
        'todos': todos,
        'teams': teams,
        'current_team_id': teamid
    })





def teams(request):
    user_team_ids = UserTeams.objects.filter(user=request.user).values_list('team_id', flat=True)
    teams = Team.objects.filter(id__in=user_team_ids)
    return render(request, "teams.html",{"teams":teams})



def edit_team(request, teamid):
    team = get_object_or_404(Team, id=teamid)
    team_members_ids = UserTeams.objects.filter(team_id=teamid).values_list("id", flat=True)
    team_members= User.objects.filter(id__in=team_members_ids)

    if request.method == "POST":
        team.team_name = request.POST.get("team_name")
        team.team_discription = request.POST.get("team_description")
        team.roll = request.POST.get("team_role")
        team.save()
        return redirect("/teams", teamid=team.id)  # or wherever you want to redirect

    return render(request, "editTeam.html", {"team": team, "team_members": team_members})


def create_team(request):
    return render(request,"createteam.html")


def notifications_list(request):
    user_notifications= Notification.objects.filter(receiver=request.user)
    return render(request,"notifications_list.html",{"user_notifications":user_notifications})




def message_view(request, messageid):
    message = get_object_or_404(Notification, id=messageid)
    return render(request , "message.html",{"message":message})