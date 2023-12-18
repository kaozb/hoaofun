from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from fun.models import Userfun


class displayall(admin.ModelAdmin):
    def get_list_filter(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

class NewUserAdmin(UserAdmin):

    fieldsets = (
        (None, {"fields": ("username","phone")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )

admin.site.register(Userfun, NewUserAdmin)