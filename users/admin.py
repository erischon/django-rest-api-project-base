from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from users import models


class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["email", "name", "is_active", "is_staff"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Informations Personnelles"), {"fields": ("name",)}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser")}),
        (_("Dates Importantes"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )


admin.site.register(models.User, UserAdmin)
