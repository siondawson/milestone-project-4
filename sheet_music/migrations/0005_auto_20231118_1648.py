# Generated by Django 3.0.1 on 2023-11-18 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet_music', '0004_auto_20231111_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sheetmusic',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
