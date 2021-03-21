from django.contrib import admin
from .models import User, UserApp, GroupApp
admin.site.register(User)

admin.site.register(UserApp)
admin.site.register(GroupApp)



