# todolist/run_migrations.py

import django
import os
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

call_command("migrate")
