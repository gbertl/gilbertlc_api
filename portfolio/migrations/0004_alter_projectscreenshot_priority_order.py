# Generated by Django 3.2.6 on 2021-08-26 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20210826_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectscreenshot',
            name='priority_order',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
