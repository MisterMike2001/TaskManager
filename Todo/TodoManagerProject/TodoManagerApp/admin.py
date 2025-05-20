from django.contrib import admin
from .models import Todo,AccountInfo, Team, UserTeams, Notification

# Register your models here.
admin.site.register(Todo)
admin.site.register(AccountInfo)
admin.site.register(Team)
admin.site.register(UserTeams)
admin.site.register(Notification)