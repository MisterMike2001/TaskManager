from django.urls import include, path
from . import views

urlpatterns=[
    path("home/", views.home, name="home"),
    path("todo/", views.todo_board,name = "todo-board"),
    path("teamboard/<int:teamid>", views.team_board,name = "team-board"),
    path("todoitem/<int:ID>/", views.todo_item , name = "todo-item"),
    path("addTask/", views.todo_add , name = "todo-add"),
    path("teams/", views.teams , name = "teams"),
    path("editteam/<int:teamid>",views.edit_team, name="edit-team"),
    path("createteam/",views.create_team, name="create-team"),
    path("notifications/",views.notifications_list, name="notifications-list"),
    path("messages/<int:messageid>",views.message_view, name="message"),
]