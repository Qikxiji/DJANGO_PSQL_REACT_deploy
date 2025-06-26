These files are linked to the secrets section in the compose.yaml file.
If you change the location of the secret files, make changes to the compose.yaml file to the section:

current compose file fragment:
------------------------------------
secrets:
  django_pass:
    file: ./environment/django_pass
  psql_pass:
    file: ./environment/psql_pass
------------------------------------

If you change the name of the secrets,
you need to make changes to the Django configuration files:

in file:
apps/backend/custom_commands/management/commands/superuser.py
in str:
DJANGO_SUPERUSER_PASSWORD = load_secret('/run/secrets/django_pass')

and in file: apps/backend/backend/settings.py
in str:
POSTGRES_PASSWORD = load_secret('/run/secrets/psql_pass')

update paths to actual (sorry, links to the secret files are HARDCODE).