from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)


class Person(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
