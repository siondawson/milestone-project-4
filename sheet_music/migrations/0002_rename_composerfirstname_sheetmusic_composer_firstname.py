# Generated by Django 3.2.23 on 2023-11-08 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheet_music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sheetmusic',
            old_name='composerfirstname',
            new_name='composer_firstname',
        ),
    ]