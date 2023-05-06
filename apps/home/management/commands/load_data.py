import os
import json

from tqdm import tqdm

from django.core.management.base import CommandError
from django.core.management.commands import loaddata
from django.conf import settings
from django.contrib.auth import get_user_model

from apps.utils.fixtures import generate_data

User = get_user_model()
FIXTURE_DIR = os.path.join(settings.BASE_DIR, 'fixtures')


class Command(loaddata.Command):
    help = 'genarate initial data for db (users, products, categories) in format json'

    def handle(self, *args, **options) -> None:
        if not FIXTURE_DIR in settings.FIXTURE_DIRS:
            raise CommandError("Please add a list of FIXTURE_DIRS in the settings.py file with the value: %s" % FIXTURE_DIR)
        
        if not os.path.exists(FIXTURE_DIR):
            os.mkdir(FIXTURE_DIR)
        
        # create superuser
        if not User.objects.filter(email=settings.ADMIN_EMAIL).exists():
            user = User.objects.create_superuser(
                first_name=settings.ADMIN_FIRST_NAME,
                last_name=settings.ADMIN_LAST_NAME,
                email=settings.ADMIN_EMAIL,
                password=settings.ADMIN_PASSWORD,
            )
            user.profile.is_fixture = True
            user.profile.bio = "CEO of Mackdin | Django & React Developer"
            user.profile.img_profile_str = "https://res.cloudinary.com/doysjtoym/image/upload/v1/cloneTwitter/media/profile/20048676-100625755915_2-s5-v1_lcfgqw"
            user.profile.save()


        count = User.objects.count()
        data = generate_data(count+1)

        with open(f"{FIXTURE_DIR}/initial_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
        
        super().handle(*args, **options)

        for user in tqdm(User.objects.all()):
            if not user.is_superuser:
                user.set_password(user.password)
                user.save()