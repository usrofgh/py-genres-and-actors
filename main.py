import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]

    actors = [
        "George Klooney",
        "Kianu Reaves",
        "Scarlett Keegan",
        "Will Smith",
        "Jaden Smith",
        "Scarlett Johansson"
    ]

    genre = Genre.objects
    actor = Actor.objects

    for genre_name in genres:
        genre.create(name=genre_name)

    for actor_full_name in actors:
        first_name, last_name = actor_full_name.split()
        actor.create(
            first_name=first_name,
            last_name=last_name,
        )

    genre.filter(name="Dramma").update(name="Drama")
    actor.filter(first_name="George", last_name="Klooney").update(last_name="Clooney")
    actor.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")

    genre.filter(name="Action").delete()
    actor.filter(first_name="Scarlett").delete()

    return actor.filter(last_name="Smith").order_by("first_name").values()


if __name__ == '__main__':
    print(main())
