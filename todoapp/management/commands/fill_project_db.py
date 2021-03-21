from django.core.management.base import BaseCommand

import json
import os

from mimesis import Person, Text
from datetime import datetime

from todoapp.models import Project, ToDo, Author

COUNT_ELEM = 3  # Кол-во элементов

class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):

        # Fill users and authors
        Project.objects.all().delete()

        text_ru = Text('ru')
        text_en = Text('en')

        for inx in range(COUNT_ELEM):
            project = {
                'name': text_ru.title(),
                'repository_url': f'htts://localhost/{inx}'
            }
            new_project = Project(**project)
            new_project.save()
            print(f'Created: project {project["name"]}')

            author = Author.objects.all()[0]
            print(author)
            for _ in range(10):
                todo = {
                    'project': new_project,
                    'text': text_en.text(quantity=1),
                    'author': author,
                    'is_active': True
                }
                new_todo = ToDo(**todo)
                new_todo.save()




