from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager


# Create your models here.
class MyUser(AbstractBaseUser):
    email = models.EmailField(_("e-mail"), unique=True, blank=True, null=True)
    phone = models.CharField(
        _("phone number"), unique=True, max_length=30, blank=True, null=True
    )

    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), blank=True, null=True, max_length=50)
    country = models.CharField(_("country"), blank=True, null=True, max_length=5)

    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    last_login = models.DateTimeField(_("last login"), auto_now=True)
    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(_("staff"), default=False)
    is_seller = models.BooleanField(_("seller"), default=False)
    is_superuser = models.BooleanField(_("superuser"), default=False)

    USERNAME_FIELD = "phone"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    # def get_email_field_name(self):
    #     return self.EMAIL_FIELD

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    # def get_username(self):
    #     return self.username

    def __str__(self) -> str:
        if not self.email:
            return f"{self.first_name} {self.last_name}"
        return self.email

    # this methods are require to login super user from admin panel
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    # this methods are require to login super user from admin panel
    def has_module_perms(self, app_label):
        return self.is_superuser


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField()
    date_of_birth = models.DateField(_("date of birth"), blank=True, null=True)
