# Generated by Django 3.2.6 on 2022-02-12 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20211101_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='priority_order',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
