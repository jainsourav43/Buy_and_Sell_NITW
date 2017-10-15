from django.contrib import admin

# Register your models here.
from .models import UserProfile
from .models import item
admin.site.register(UserProfile)
admin.site.register(item)