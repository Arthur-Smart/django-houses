from django.contrib import admin

from .models import Category, House, Booked_house

admin.site.register(Category)
admin.site.register(House)
admin.site.register(Booked_house)