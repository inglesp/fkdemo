from django.core.management import BaseCommand
from ...models import Person


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("name")

    def handle(self, name, **options):
        p = Person.objects.get(name=name)
        print(f"{p.id=}")
        print(f"{p.name=}")
        print(f"{p.team_id=}")
        print(f"{p.team.pk=}")
        print(f"{p.team.id=}")
        print(f"{p.team.name=}")
