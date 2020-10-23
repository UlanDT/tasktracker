from django.db import models
from users.models import Member
from django.utils import timezone


class Status(models.TextChoices):
    TD = "TD", "To Do"
    WIP = "WIP", "Work In Progress"
    RW = "RW", "Review"
    DONE = "DONE", "Done"


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    team_member = models.ManyToManyField(to=Member, related_name="team_member")
    spectator = models.ManyToManyField(to=Member, related_name="spectator")
    status = models.CharField(max_length=4, choices=Status.choices)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(blank=True, null=True)
    estimated_time = models.DateTimeField()


class CheckList(models.Model):
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE)
    title = models.TextField()


