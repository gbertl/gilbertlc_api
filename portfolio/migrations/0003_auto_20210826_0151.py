# Generated by Django 3.2.6 on 2021-08-26 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210826_0151'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectScreenshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority_order', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.project')),
                ('screenshot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.screenshot')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='screenshots',
            field=models.ManyToManyField(through='portfolio.ProjectScreenshot', to='portfolio.Screenshot'),
        ),
    ]
