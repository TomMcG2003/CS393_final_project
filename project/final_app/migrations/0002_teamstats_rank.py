# Generated by Django 4.2.16 on 2024-11-22 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamstats',
            name='rank',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
