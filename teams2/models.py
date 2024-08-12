from django.db import models


class Team(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)


class Person(models.Model):
    name = models.CharField(max_length=100)
    team_code = models.CharField(max_length=3)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
