# Generated by Django 3.1.7 on 2021-03-12 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leBeau', '0003_auto_20210312_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='selling_date',
            field=models.DateField(default='-', null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='selling_price',
            field=models.IntegerField(default='-', null=True),
        ),
    ]