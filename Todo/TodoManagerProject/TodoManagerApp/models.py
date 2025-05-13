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



