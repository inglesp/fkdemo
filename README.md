This project shows three ways of linking Django models via foreign keys.

There are three apps (`teams1`, `teams2`, `teams3`),
each of which has a `Team` and a `Person` model.
Persons belong to teams, and a team has many persons.

Each app has a management command for importing teams and persons,
and a management command for reporting the details of a single person.

For instance, run:

```
./manage.py import1
./manage.py report1 Peter
```
