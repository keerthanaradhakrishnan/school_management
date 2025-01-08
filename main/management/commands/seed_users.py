import sys
from django.core.management.base import BaseCommand
from main.models import CustomUser

class Command(BaseCommand):
    help = "Seed database with default user roles"

   def handle(self, *args, **kwargs):
    users = [
        {'username': 'admin', 'password': 'admin123', 'role': 'admin'},
        {'username': 'officestaff', 'password': 'office123', 'role': 'office'},
        {'username': 'librarian', 'password': 'lib123', 'role': 'librarian'},
    ]

    for user_data in users:
        username = user_data['username']
        password = user_data['password']
        role = user_data['role']

        if role == 'admin':
            # Check if the superuser already exists
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username=username, password=password)
                print(f"Superuser '{username}' created.")
            else:
                print(f"Superuser '{username}' already exists.")
        else:
            # Check if a normal user with the same username exists
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, password=password)
                print(f"User '{username}' created with role '{role}'.")
            else:
                print(f"User '{username}' already exists.")
