# Generated by Django 4.0.5 on 2022-09-19 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_customuser_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_superuser',
        ),
    ]
