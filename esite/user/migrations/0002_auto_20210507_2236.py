# Generated by Django 3.1.10 on 2021-05-07 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snekuser',
            name='address',
        ),
        migrations.RemoveField(
            model_name='snekuser',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='snekuser',
            name='city',
        ),
        migrations.RemoveField(
            model_name='snekuser',
            name='country',
        ),
        migrations.RemoveField(
            model_name='snekuser',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='snekuser',
            name='telephone',
        ),
    ]
