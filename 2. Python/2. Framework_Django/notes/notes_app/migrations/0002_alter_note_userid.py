# Generated by Django 3.2.3 on 2022-12-21 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='UserID',
            field=models.IntegerField(null=True),
        ),
    ]
