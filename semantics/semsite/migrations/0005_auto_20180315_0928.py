# Generated by Django 2.0.2 on 2018-03-15 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semsite', '0004_auto_20180315_0900'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='handbookarticle',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='idea',
            options={'verbose_name': 'Идея', 'verbose_name_plural': 'Идеи'},
        ),
        migrations.AlterModelOptions(
            name='term',
            options={'verbose_name': 'Термин', 'verbose_name_plural': 'Термины'},
        ),
    ]