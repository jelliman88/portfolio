# Generated by Django 3.1.7 on 2021-04-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leBeau', '0006_transaction_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='profit',
            field=models.IntegerField(null=True),
        ),
    ]
