# Generated by Django 3.2.15 on 2022-09-28 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0002_alter_track_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]