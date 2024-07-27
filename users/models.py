from django.apps import apps
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("Необходимо задать имя пользователя")

        user_model = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = user_model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("Имя пользователя"),
        max_length=150,
        unique=True,
        help_text=_(
            "Обязательное поле. 150 символов и меньше. Только буквы, цифры и @/./+/-/_."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("Пользователь с таким именем уже существует."),
        },
    )
    is_staff = models.BooleanField(
        _("Статус редактора"),
        default=False,
        help_text=_("Роль редактора. Может добавлять и изменять научные материалы"),
    )
    is_active = models.BooleanField(
        _("Активная учетная запись"),
        default=True,
        help_text=_("Статус активной учетной записи. Отключает процедуру аутентификации"),
    )
    is_superuser = models.BooleanField(
        _("Статус администратора"),
        default=False,
        help_text=_("Роль администратора. Может управлять пользователями и научными материалами"),
    )
    date_joined = models.DateTimeField(_("Дата регистрации"), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.id} | {self.username}"

    class Meta:
        verbose_name = _("пользователь")
        verbose_name_plural = _("пользователи")
