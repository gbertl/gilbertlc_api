# Generated by Django 3.2.6 on 2021-08-26 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='technology',
            options={'verbose_name_plural': 'technologies'},
        ),
        migrations.RemoveField(
            model_name='project',
            name='screenshots',
        ),
    ]
