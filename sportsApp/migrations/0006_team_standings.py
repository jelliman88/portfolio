# Generated by Django 3.1.7 on 2021-04-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0005_auto_20210403_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='standings',
            field=models.TextField(default='[]'),
        ),
    ]
