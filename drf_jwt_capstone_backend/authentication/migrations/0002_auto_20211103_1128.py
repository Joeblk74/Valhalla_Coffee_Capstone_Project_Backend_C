# Generated by Django 3.2.8 on 2021-11-03 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='middle_name',
        ),
        migrations.AddField(
            model_name='user',
            name='prefix',
            field=models.CharField(default='Mr', max_length=5),
            preserve_default=False,
        ),
    ]
