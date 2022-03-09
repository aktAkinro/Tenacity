from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin #this is to avoid a name clash with useradmin below
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import User


# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name'),
        }),
    )
