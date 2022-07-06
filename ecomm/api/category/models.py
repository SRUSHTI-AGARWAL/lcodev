from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# This constructor is created to diplay name instead of Category object 1 and object 2 in admin panel

    def __str__(self):
        return self.name

# These records of table are for audit purpose only. not supposed to be shown to admin or normal users unless required.

# auto_now_add is the current server timestamp of creating the data-row in DB. Strictly for creation.

#auto_now does exactlythe same, but user for updating the value as this field of updated_at will change
# every now and then based on the data that we enter and update in the admin panel.



