from django.contrib import admin

# Register your models here.
from users.models import User, Locations

admin.site.register(User)
admin.site.register(Locations)