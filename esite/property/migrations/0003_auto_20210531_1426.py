# Generated by Django 3.1.10 on 2021-05-31 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20210531_1426'),
        ('documents', '0001_initial'),
        ('property', '0002_space_tenants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='featured_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.snekimage'),
        ),
        migrations.AlterField(
            model_name='property',
            name='image_gallery',
            field=models.ManyToManyField(related_name='_property_image_gallery_+', to='images.SNEKImage'),
        ),
        migrations.AlterField(
            model_name='space',
            name='contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='documents.snekdocument'),
        ),
        migrations.AlterField(
            model_name='space',
            name='docs',
            field=models.ManyToManyField(related_name='_space_docs_+', to='documents.SNEKDocument'),
        ),
        migrations.AlterField(
            model_name='space',
            name='featured_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.snekimage'),
        ),
        migrations.AlterField(
            model_name='space',
            name='image_gallery',
            field=models.ManyToManyField(related_name='_space_image_gallery_+', to='images.SNEKImage'),
        ),
    ]