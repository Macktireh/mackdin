from datetime import timedelta
from random import randint

from django.utils import timezone
from faker import Faker

from apps.utils.function import uid_gerator


fake = Faker(locale="fr_FR")
# fake = Faker()

users_data = []

list_email_unique = [fake.unique.email() for _ in range(200)]
# list_phone_number_unique = [fake.unique.phone_number() for _ in range(11, 101)]

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
    profile_data.append(
        {
            "model": "profiles.Profile",
            "pk": i + 2,
            "fields": {
                "uid": f"{uid_gerator()}",
                "user_id": f"{i + 2}",
                "pseudo": f"{pseudo}",
                "bio": f"{fake.text(80)}",
                "birth_date": fake.date_time_between(start_date="-50y", end_date="-18y").strftime("%Y-%m-%d"),
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
            },
        }
    )

data = users_data + profile_data