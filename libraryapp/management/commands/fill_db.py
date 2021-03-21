from django.core.management.base import BaseCommand

import json
import os

from mimesis import Person, Text
from datetime import datetime

from libraryapp.models import Author, Article
from authapp.models import User, UserApp

COUNT_ELEM = 100 # Кол-во элементов
LANG = "en"

JSON_PATH = 'libraryapp/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)

class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):

        # Fill users and authors
        Article.objects.all().delete()
        Author.objects.all().delete()
        UserApp.objects.all().delete()

        text = Text(LANG)
        person = Person(LANG)

        for _ in range(COUNT_ELEM):
            first_name = person.first_name()
            last_name = person.last_name()
            login = f'{first_name}.{last_name}'
            email = person.email()
            birthday_year = datetime.today().year-person.age(minimum=14, maximum=100)
            print(f'Created:{login} - {email}')
            user = {
                    "login": login,
            }
            new_user = UserApp(**user)
            new_user.save()
            author = {
                "user": new_user,
                "first_name": first_name,
                "last_name": last_name,
                "birthday_year": birthday_year,
            }
            new_author = Author(**author)
            new_author.save()

            article = {
                'name': text.title(),
                'text': text.text(quantity=50),
                'author': new_author
            }
            new_article = Article(**article)
            new_article.save()


        # Creating django admin user
        User.objects.all().delete()
        User.objects.create_superuser('admin', 'admin@localhost', 'admin')

        import todoapp.management.commands.fill_project_db

