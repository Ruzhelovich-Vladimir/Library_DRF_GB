from django.contrib import admin
from .models import Author, Biography, Book, Article

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Biography)
admin.site.register(Article)

