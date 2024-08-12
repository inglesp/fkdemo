from django.core.management import BaseCommand
from ...models import Team, Person


class Command(BaseCommand):
    def handle(self, **options):
        Person.objects.all().delete()
        Team.objects.all().delete()

        rap_team = Team.objects.create(name="RAP Team")
        rex_team = Team.objects.create(name="REX Team")

        # Here's one way of creating Person objects directly
        for name in ["Becky", "Dave", "Peter", "Providence", "Simon", "Tom"]:
            Person.objects.create(name=name, team=rap_team)

        # And here's another way
        for name in ["Iain", "Jon", "Lucy", "Steve", "Thomas"]:
            Person.objects.create(name=name, team_id=rex_team.id)

        # We can also create Person objects without a corresponding Team, but
        # note that this requires that we have `null=True` in the definition of
        # Person.team
        Person.objects.create(name="Ben")
