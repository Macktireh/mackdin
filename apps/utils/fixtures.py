from datetime import timedelta
from random import randint, sample

from django.utils import timezone
from faker import Faker

from apps.utils.function import uid_gerator


fake = Faker(locale="fr_FR")

users_data = []

list_email_unique = [fake.unique.email() for _ in range(200)]
# list_phone_number_unique = [fake.unique.phone_number() for _ in range(11, 101)]


def random_numbers(low, high, n):
    return sample(range(low, high), n)


for i, email in enumerate(list_email_unique):
    # email = _email.split("@")[0] + str(i + 2) + "@" + _email.split("@")[1]
    password = email.split("@")[0]
    users_data.append(
        {
            "model": "users.CustomUser",
            "pk": i + 2,
            "fields": {
                "email": email,
                "first_name": f"{fake.first_name()}",
                "last_name": f"{fake.last_name()}",
                "is_email_verified": True,
                "password": f"{password}",
            },
        }
    )


profile_data = []

for i, user in enumerate(users_data):
    pseudo = user["fields"]["email"].split("@")[0]
    friends = random_numbers(1, len(users_data) - 1, randint(20, 50))
    if i + 2 in friends:
        friends.remove(i + 2)
    profile_data.append(
        {
            "model": "profiles.Profile",
            "pk": i + 2,
            "fields": {
                "uid": f"{uid_gerator()}",
                "user_id": f"{i + 2}",
                "pseudo": f"{pseudo}",
                "bio": f"{fake.text(80)}",
                "birth_date": fake.date_time_between(
                    start_date="-50y", end_date="-18y"
                ).strftime("%Y-%m-%d"),
                "img_profile_str": f"{fake.image_url()}",
                "img_bg_str": f"{fake.image_url()}",
                "is_fixture": True,
                "phone": f"{fake.phone_number()}",
                "phone": f"{fake.street_address()}",
                "town": f"{fake.city()}",
                "region": f"{fake.region()}",
                "zipcode": f"{fake.postcode()}",
                "country": f"{fake.country()}",
                "date_updated": str(timezone.now()),
                "friends": friends,
            },
        }
    )


post_data = []

for i in range(60):
    author_id = users_data[randint(0, len(users_data) - 1)]["pk"]
    date = str(
        timezone.now()
        + timedelta(days=randint(-50, -11))
        + timedelta(hours=randint(-9, 9))
        + timedelta(minutes=randint(-20, 20))
        + timedelta(seconds=randint(-20, 20))
    )
    post_data.append(
        {
            "model": "post.Post",
            "pk": i + 1,
            "fields": {
                "uid": f"{uid_gerator()}",
                "author_id": f"{author_id}",
                "message": f"{fake.paragraph(nb_sentences=5)}",
                "img_str": f"{fake.image_url()}",
                "is_fixture": True,
                "liked": random_numbers(1, len(users_data) - 1, randint(40, 100)),
                "date_created": date,
                "date_updated": date,
            },
        }
    )


likes_post_data = []

pks = []
for i, post in enumerate(post_data):
    for j in post["fields"]["liked"]:
        pks.append(j)
        likes_post_data.append(
            {
                "model": "post.LikePost",
                "pk": len(pks),
                "fields": {
                    "post_id": f"{post['pk']}",
                    "user_id": f"{j}",
                    "value": "Like",
                },
            }
        )


comment_data = []

pks = []
for i, post in enumerate(post_data):
    for j in range(randint(10, 40)):
        author_id = users_data[randint(0, len(users_data) - 1)]["pk"]
        date = str(
            timezone.now()
            + timedelta(days=randint(-10, 0))
            + timedelta(hours=randint(-9, 9))
            + timedelta(minutes=randint(-20, 20))
            + timedelta(seconds=randint(-20, 20))
        )
        if j == 0:
            pks.append(j)
            comment_data.append(
                {
                    "model": "comments.Comment",
                    "pk": len(pks),
                    "fields": {
                        "author_id": f"{post['fields']['author_id']}",
                        "post_id": f"{post['pk']}",
                        "message": f"{fake.paragraph(nb_sentences=2)}",
                        "liked": random_numbers(1, len(users_data) - 1, randint(1, 10)),
                        "date_added": date,
                        "date_updated": date,
                    },
                }
            )
        pks.append(j)
        comment_data.append(
            {
                "model": "comments.Comment",
                "pk": len(pks),
                "fields": {
                    "author_id": f"{author_id}",
                    "post_id": f"{post['pk']}",
                    "message": f"{fake.paragraph(nb_sentences=2)}",
                    "liked": random_numbers(1, len(users_data) - 1, randint(1, 10)),
                    "date_added": date,
                    "date_updated": date,
                },
            }
        )


likes_comment_data = []

pks = []
for i, comment in enumerate(comment_data):
    for j in comment["fields"]["liked"]:
        pks.append(j)
        likes_comment_data.append(
            {
                "model": "comments.LikeComment",
                "pk": len(pks),
                "fields": {
                    "comment_id": f"{comment['pk']}",
                    "user_id": f"{j}",
                    "value": "Like",
                },
            }
        )



relationship_data = []

pks = []
for i, profile in enumerate(profile_data):
    for j in profile["fields"]["friends"]:
        pks.append(j)
        date = str(
            timezone.now()
            + timedelta(days=randint(-22, 0))
            + timedelta(hours=randint(-9, 9))
            + timedelta(minutes=randint(-20, 20))
            + timedelta(seconds=randint(-20, 20))
        )
        sender_id = profile["pk"] if j % 2 == 0 else j
        receiver_id = j if j % 2 == 0 else profile["pk"]
        relationship_data.append(
            {
                "model": "friends.Relationship",
                "pk": len(pks),
                "fields": {
                    "sender_id": f"{sender_id}",
                    "receiver_id": f"{receiver_id}",
                    "status": "accepted",
                    "date_sender": date,
                    "date_receiver": date,
                    "date_created": date,
                    "date_updated": date,
                },
            }
        )


data = (
    users_data
    + profile_data
    + post_data
    + likes_post_data
    + comment_data
    + relationship_data
)
