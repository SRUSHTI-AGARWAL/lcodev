from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.product'


# Error thrown if Auto Field id not used:
#  Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
# HINT: Configure the DEFAULT_AUTO_FIELD setting or the ProductConfig.default_auto_field attribute to
# point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.