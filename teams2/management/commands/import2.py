from django.core.management import BaseCommand
from ...models import Team, Person


class Command(BaseCommand):
    def handle(self, **options):
        Person.objects.all().delete()
        Team.objects.all().delete()

        Team.objects.create(code="rap", name="RAP Team")
        Team.objects.create(code="rex", name="REX Team")

        for name in ["Becky", "Dave", "Peter", "Providence", "Simon", "Tom"]:
            team = Team.objects.get(code="rap")
            Person.objects.create(name=name, team_code="rap", team=team)

        for name in ["Iain", "Jon", "Lucy", "Steve", "Thomas"]:
            team = Team.objects.get(code="rex")
            Person.objects.create(name=name, team_code="rex", team=team)
