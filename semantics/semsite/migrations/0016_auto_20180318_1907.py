# Generated by Django 2.0.3 on 2018-03-18 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semsite', '0015_term_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='handbookarticle',
            name='slug',
        ),
    ]
