# Generated by Django 3.2.6 on 2021-08-28 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_project_priority_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.SlugField(unique=True),
        ),
    ]
