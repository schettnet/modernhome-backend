# Generated by Django 3.1.10 on 2021-05-07 22:01

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtaildocs', '0010_document_file_hash'),
        ('user', '0003_auto_20210507_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=40, null=True)),
                ('address', models.CharField(max_length=60, null=True)),
                ('city', models.CharField(max_length=60, null=True)),
                ('postal_code', models.CharField(max_length=12, null=True)),
                ('country', models.CharField(max_length=2, null=True)),
                ('title', models.CharField(max_length=250, null=True)),
                ('status', models.CharField(choices=[('EPH', 'EP house'), ('MPH', 'MP house'), ('DH', 'D house')], default='EPH', max_length=3)),
                ('featured_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('image_gallery', models.ManyToManyField(related_name='_property_image_gallery_+', to='wagtailimages.Image')),
                ('landlord', modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='properties', to='user.landlord')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True)),
                ('is_rental', models.BooleanField(default=True)),
                ('contract', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document')),
                ('docs', models.ManyToManyField(related_name='_space_docs_+', to='wagtaildocs.Document')),
                ('featured_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('image_gallery', models.ManyToManyField(related_name='_space_image_gallery_+', to='wagtailimages.Image')),
                ('prop', modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spaces', to='property.property')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
