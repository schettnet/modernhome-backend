# Generated by Django 3.1.10 on 2021-05-31 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20201027_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snekpersonavatarimage',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='snekpersonavatarimage',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='snekpersonavatarimage',
            name='uploaded_by_user',
        ),
        migrations.DeleteModel(
            name='SNEKAchievementImage',
        ),
        migrations.DeleteModel(
            name='SNEKPersonAvatarImage',
        ),
    ]
