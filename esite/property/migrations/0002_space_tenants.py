# Generated by Django 3.1.10 on 2021-05-07 22:06

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210507_2307'),
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='tenants',
            field=modelcluster.fields.ParentalManyToManyField(related_name='spaces', to='user.Tenant'),
        ),
    ]
