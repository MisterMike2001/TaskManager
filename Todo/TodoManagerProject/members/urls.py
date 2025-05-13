from django.urls import include, path
from . import views

urlpatterns=[
    path('login_user/',views.login_user, name="login"),
    path('logout_user/', views.logout_user, name ="logout"),
    path('account',views.Account_info, name= 'account'),
    path('register/', views.register_user, name="register"),
]