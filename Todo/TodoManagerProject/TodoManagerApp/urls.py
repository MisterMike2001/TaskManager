from django.urls import include, path
from . import views

urlpatterns=[
    path("home/", views.home, name="home"),
    path("todo/", views.todo_board,name = "todo-board"),
    path("todoitem/<int:ID>/", views.todo_item , name = "todo-item"),
    path("addTask/", views.todo_add , name = "todo-add"),
    path("account/", views.Account, name= "account"),
]