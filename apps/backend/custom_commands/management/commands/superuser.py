from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth import get_user_model

from decouple import config

import os

DJANGO_SUPERUSER_USERNAME = config('DJANGO_SUPERUSER_USERNAME', cast=str)
DJANGO_SUPERUSER_EMAIL = config('DJANGO_SUPERUSER_EMAIL', cast=str)

#uncomment if password in .env file
#DJANGO_SUPERUSER_PASSWORD = config('DJANGO_SUPERUSER_PASSWORD', cast=str)

#GET PASSWORD FROM SECRET FILE. BE CAREFUL WHEN CHANGE SOMETHING IN SECRETS!!!
#-----------------------------------------------------------------------------
def load_secret(key_file_path):
    if not key_file_path or not os.path.exists(key_file_path):
        return None
    
    with open(key_file_path, 'r') as f:
        value = f.read().strip()
        return value

DJANGO_SUPERUSER_PASSWORD = load_secret('/run/secrets/django_pass')

if DJANGO_SUPERUSER_PASSWORD is not None:
    os.environ['DJANGO_SUPERUSER_PASSWORD'] = DJANGO_SUPERUSER_PASSWORD
#-----------------------------------------------------------------------------



class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        try:
            User = get_user_model()
            user = User(
                email=DJANGO_SUPERUSER_EMAIL,
                username=DJANGO_SUPERUSER_USERNAME,
            )
            user.set_password(DJANGO_SUPERUSER_PASSWORD)
            user.is_superuser = True
            user.is_staff = True
            user.is_admin = True
            user.save()
            self.stdout.write(self.style.SUCCESS('Successfully created new superuser'))
        except Exception as e:
            raise CommandError(e)
        