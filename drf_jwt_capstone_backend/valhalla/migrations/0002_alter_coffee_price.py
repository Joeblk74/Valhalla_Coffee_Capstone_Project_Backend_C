# Generated by Django 3.2.8 on 2021-11-03 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valhalla', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='price',
            field=models.IntegerField(),
        ),
    ]