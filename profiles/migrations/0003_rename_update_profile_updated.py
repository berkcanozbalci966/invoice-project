# Generated by Django 4.0.2 on 2022-02-21 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_rename_account_user_profile_account_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='update',
            new_name='updated',
        ),
    ]
