# Generated by Django 4.0.2 on 2022-02-28 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.SmallIntegerField(default=2016),
            preserve_default=False,
        ),
    ]