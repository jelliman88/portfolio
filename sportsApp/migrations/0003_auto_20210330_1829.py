# Generated by Django 3.1.7 on 2021-03-30 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0002_auto_20210330_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.ImageField(upload_to='sportsApp/logos'),
        ),
    ]
