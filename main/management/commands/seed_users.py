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

        for user in users:
            if not CustomUser.objects.filter(username=user['username']).exists():
                CustomUser.objects.create_user(
                    username=user['username'],
                    password=user['password'],
                    role=user['role']
                )
                self.stdout.write(self.style.SUCCESS(f"User {user['username']} created."))
            else:
                self.stdout.write(self.style.WARNING(f"User {user['username']} already exists."))
