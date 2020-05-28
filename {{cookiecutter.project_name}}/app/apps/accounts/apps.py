from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccountsConfig(AppConfig):
    """Accounts application."""

    name = "apps.accounts"
    verbose_name = _("Accounts")
