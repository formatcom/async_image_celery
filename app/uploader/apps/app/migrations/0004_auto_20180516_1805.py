# Generated by Django 2.0.1 on 2018-05-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180516_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='priority',
            field=models.PositiveIntegerField(default=0, editable=False, unique=True),
        ),
    ]