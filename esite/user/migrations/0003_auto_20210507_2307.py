# Generated by Django 3.1.10 on 2021-05-07 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210507_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.snekuser')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.snekuser')),
            ],
        ),
        migrations.AddField(
            model_name='snekuser',
            name='address',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='snekuser',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='snekuser',
            name='city',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='snekuser',
            name='company_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='snekuser',
            name='company_vat',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='snekuser',
            name='country',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='snekuser',
            name='postal_code',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='snekuser',
            name='telephone',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
