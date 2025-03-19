from django.contrib import admin
from django.contrib.auth.models import User

from restapp.models import *
# Register your models here.

admin.site.register(table)
admin.site.register(contact)