from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser):

    name = models.CharField(max_length=50,default='Anonymous')
    email = models.EmailField(max_length=250,unique=True)  #for every user to be unique, unique= True
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')

    # marking this as None as we would not be signing-in using username but rather using email.
    # # In django default sign-in uses Username to sign in,but we will be using Email for other user to sign-in.

    username = None
    USERNAME_FIELD = 'email'  # username field will be validated now by email
    REQUIRED_FILEDS =[]


# just adding more information, but above code is sufficient to sign-in user using email.
    phone = models.CharField(max_length=50,blank=True,null=True)
    gender = models.CharField(max_length=10,blank=True,null=True)

    # passing blank as true makes this field optional and these details can go empty into the DB

    session_token = models.CharField(max_length=10,default=0)
    # django does not work with token base, authentication here is different.But we will be generating our custom token here.

    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #django does not work on token based but we will be generating our custom tokens as we will work on session based token.
# default= 0 means user is not logged in and it can be empty string also
# Create your models here.

    objects = CustomUserManager()
    def get_username(self):
        return self.email

    # @property
    # def is_superuser(self):
    #     return self.is_admin


    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, add_label):
        return True
