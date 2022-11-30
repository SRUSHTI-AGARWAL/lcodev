from django.db import migrations
from api.user.models import CustomUser



class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user= CustomUser(name='srishti',
                         email ='srish@lco.dev',
                         is_staff=True,
                         is_superuser=True,
                         phone='838338882821',
                         gender='Female')
        user.set_password("56789")    # saving data in DB.
        user.save()

    dependencies = [
        # ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [

        migrations.RunPython(seed_data),
        ]

#
# todo >why 0001_initial only in "api-migrations" and not in any other app?
#
# because api is parent folder and 0001_migrations is present in all other apps which are generated
# automatically when we run migrations but we added one manually to control fields of django superuser.
