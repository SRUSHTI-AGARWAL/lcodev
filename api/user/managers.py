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
        """
        Create and save a SuperUser with the given email and password.
        """
        # extra_fields.setdefault("is_staff", True)
        # extra_fields.setdefault("is_superuser", True)
        # extra_fields.setdefault("is_active", True)

        # if extra_fields.get("is_staff") is not True:
        #     raise ValueError("Superuser must have is_staff=True.")
        # if extra_fields.get("is_superuser") is not True:
        #     raise ValueError("Superuser must have is_superuser=True.")
        user = self.create_user(
            email,
            password,
        )
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save()
        return user

    # def get_full_name(self):
    #     '''
    #     Returns the first_name plus the last_name, with a space in between.
    #     '''
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()
    #
    # def get_short_name(self):
    #     '''
    #     Returns the short name for the user.
    #     '''
    #     return self.first_name
    #
