from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from users.forms import CustomUserChangeForm, CustomUserCreationForm
from users.models import User
from django.contrib.auth.admin import UserAdmin


class CustomAdminSite(admin.AdminSite):
    site_header = 'Административная панель библиотеки "ВИТ ЭРА"'
    site_title = 'Администрирование библиотека "ВИТ ЭРА"'

    def has_permission(self, request):
        return request.user.is_active and request.user.is_superuser


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Роли"),
         {
             "fields": ("is_active", "is_staff", "is_superuser",),
         },
         ),
        (_("Временные данные"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "is_staff", "is_active", 'is_superuser'),
            },
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ("username", "is_staff", "is_superuser", 'is_active')
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username",)
    readonly_fields = ('last_login', 'date_joined')


admin_site = CustomAdminSite(name='admin')

admin_site.register(User, CustomUserAdmin)
admin_site.register(Group)
