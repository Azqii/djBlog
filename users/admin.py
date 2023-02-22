from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Profile
from .forms import UserRegisterForm

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )

    add_form = UserRegisterForm

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
