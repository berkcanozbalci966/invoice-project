# Generated by Django 4.0.2 on 2022-02-23 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_rename_update_profile_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='images/avatar.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='company_logo',
            field=models.ImageField(default='images/no_photo.png', upload_to=''),
        ),
    ]
