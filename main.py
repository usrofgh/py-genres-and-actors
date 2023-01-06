import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:
    
    genre = Genre.objects
    actor = Actor.objects

    genre.create(name="Western")
    genre.create(name="Action")
    genre.create(name="Dramma")

    actor.create(first_name="George", last_name="Klooney")
    actor.create(first_name="Scarlett", last_name="Keegan")
    actor.create(first_name="Kianu", last_name="Reaves")
    actor.create(first_name="Will", last_name="Smith")
    actor.create(first_name="Jaden", last_name="Smith")
    actor.create(first_name="Scarlett", last_name="Johansson")

    genre.filter(name="Dramma").update(name="Drama")
    actor.filter(first_name="George", last_name="Klooney").update(last_name="Clooney")
    actor.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")

    genre.filter(name="Action").delete()
    actor.filter(first_name="Scarlett").delete()

    return actor.filter(last_name="Smith").order_by("first_name").values()


if __name__ == '__main__':
    print(main())
