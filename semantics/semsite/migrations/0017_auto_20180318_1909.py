# Generated by Django 2.0.3 on 2018-03-18 16:09

import autoslug.fields
from django.db import migrations
import semsite.models

def migrate_data_forward(apps, schema_editor):
    for instance in semsite.models.Author.objects.all():
        print("Generating slug for %s"%instance)
        instance.save()
    for instance in semsite.models.HandbookArticle.objects.all():
        print("Generating slug for %s"%instance)
        instance.save()

def migrate_data_backward(apps, schema_editor):
    pass




class Migration(migrations.Migration):

    dependencies = [
        ('semsite', '0016_auto_20180318_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from=semsite.models.Author.slugify, unique=True),
        ),
        migrations.AddField(
            model_name='handbookarticle',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from=semsite.models.HandbookArticle.slugify, unique=True),
        ),
        migrations.RunPython(
            migrate_data_forward,
            migrate_data_backward,
        ),

    ]
