# Generated by Django 2.0.2 on 2018-03-15 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semsite', '0003_auto_20180315_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='description',
            field=models.TextField(verbose_name='Определение'),
        ),
    ]