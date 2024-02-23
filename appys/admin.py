from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Plant)

admin.site.register(Account)

admin.site.register(UserProfile)

admin.site.register(Tree)

admin.site.register(Location)



