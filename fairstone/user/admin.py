from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FairstoneUser


class FairstoneUserAdmin(UserAdmin):
    model = FairstoneUser


admin.site.register(FairstoneUser, FairstoneUserAdmin)
