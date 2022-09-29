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

