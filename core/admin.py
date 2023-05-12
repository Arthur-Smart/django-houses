from django.contrib import admin

from .models import Userprofile, Properties, Like
# Register your models here.
admin.site.register(Userprofile)
admin.site.register(Properties)
admin.site.register(Like)