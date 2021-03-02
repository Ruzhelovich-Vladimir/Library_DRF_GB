from django.core.management.base import BaseCommand
from libraryapp.models import Author
from authapp.models import UserProfile, User
import json
import os
from mimesis import Person
from datetime import datetime

COUNT_ELEM = 20


JSON_PATH = 'libraryapp/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        UserProfile.objects.all().delete()
        Author.objects.all().delete()

        person = Person('en')

        for _ in range(COUNT_ELEM):
            first_name = person.first_name()
            last_name = person.last_name()
            login = f'{first_name}.{last_name}'
            email = person.email()
            birthday_year = datetime.today().year-person.age(minimum=14, maximum=100)
            print(f'Created:{login} - {email}')
            user = {
                    "user_name": login,
                    "first_name": first_name,
                    "last_name": last_name,
                    "gender": person.sex('M', 'F'),
                    "birthday_year": birthday_year,
                    "email": email
            }
            author = {
                "first_name": first_name,
                "last_name": last_name,
                "birthday_year": birthday_year,
            }
            new_user = UserProfile(**user)
            new_user.save()
            new_author = Author(**author)
            new_author.save()

        User.objects.all().delete()
        User.objects.create_superuser('admin', 'admin@localhost', 'admin')
        

