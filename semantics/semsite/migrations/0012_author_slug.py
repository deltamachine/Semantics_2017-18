# Generated by Django 2.0.3 on 2018-03-18 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semsite', '0011_remove_author_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]