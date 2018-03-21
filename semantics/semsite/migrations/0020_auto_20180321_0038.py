# Generated by Django 2.0.2 on 2018-03-20 21:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semsite', '0019_auto_20180320_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='term',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Определение'),
        ),
    ]