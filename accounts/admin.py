from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChageForm, CustomUserCreationForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChageForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "is_superuser",
        "first_name",
        "last_name",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
