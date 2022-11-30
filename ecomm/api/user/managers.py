from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import ugettext_lazy as _

"""  
    Custom user model manager where email is the unique identifiers  
    for authentication instead of usernames.  
    """


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):

        user = self.create_user( email,
            password,
                                 )
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True

        user.save()
        return user

