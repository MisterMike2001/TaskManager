from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AccountInfo(models.Model):
    name= models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    cellphone= models.IntegerField()
    email=models.CharField(max_length=200)

class Todo(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('queued', 'Queued'),
            ('in_progress', 'In Progress'),
            ('completed', 'Completed')
        ],
        default='queued'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    teamID = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)

class Team(models.Model):
    team_name = models.CharField(max_length=200)
    team_discription = models.CharField(max_length=200)
    roll= models.CharField(max_length=100)

class UserTeams(models.Model):
    team=models.ForeignKey('Team',on_delete=models.CASCADE,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True )




class Notification(models.Model):
    sender = models.ForeignKey(User, related_name="sent_notifications", on_delete=models.SET_NULL, null=True, blank=True)
    receiver = models.ForeignKey(User, related_name="received_notifications", on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"From {self.sender} to {self.receiver}: {self.message[:50]}"