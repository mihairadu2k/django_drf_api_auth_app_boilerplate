from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.utils.translation import ugettext_lazy as _
from .manager import manager


class User(AbstractBaseUser, PermissionsMixin):
    TITLES = (
        ("Mr.", "Mr."),
        ("Ms.", "Ms."),
        ("Mrs.", "Mrs."),
        ("Miss", "Miss"),
        ("Mx.", "Mx."),
    )

    SEX = (
        ("F", "Feminine"),
        ("M", "Masculine"),
        ("O", "Prefer not to state"),
    )

    ROLES = (
        ("PRODUCT_MANAGER", "Product Manager"),
        ("SALES_COUNTRY", "Country Sales Manager"),
        ("SALES_MANAGER", "Area Sales Manager"),
        ("SALES_REGIONAL", "Regional Sales Manager"),
    )

    email = models.EmailField(_('Email address'), unique=True, blank=False)
    username = models.CharField(max_length=30, default="User")
    first_name = models.CharField(_('first name'), max_length=50, blank=True, default="Jo")
    last_name = models.CharField(_('last name'), max_length=50, blank=True, default="Doe")
    title = models.CharField(_("title"), max_length=20, blank=True, default="Mr.", choices=TITLES)
    sex = models.CharField(_("sex"), max_length=2, blank=True, default="O", choices=SEX)
    image_url = models.URLField(_("Image Url"), blank=True, null=True)

    # permissions verification
    role = models.CharField(_("Role"), choices=ROLES, max_length=50, null=False)
    country = models.CharField(_("Country"), max_length=100, default="Germany") # todo country field based on SOCO DB
    area = models.CharField(_("Area"), max_length=100, default="DACH") # todo area field based on SOCO DB
    region = models.CharField(_("Region"), max_length=100, default="Europe") # todo region field based on SOCO DB
    date_joined = models.DateTimeField(_("Date joined"), auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = manager.UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('last_name', 'first_name', 'role')

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        app_label = 'api_auth'

    def get_full_name(self):
        """
        Used to get a users full name
        """
        return self.last_name + self.first_name

    def get_short_name(self):
        """
           Used to get a users short name
        """
        return self.last_name

    def __str__(self):
        return self.email


