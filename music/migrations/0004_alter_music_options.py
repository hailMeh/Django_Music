# Generated by Django 4.0.4 on 2022-05-14 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_music_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='music',
            options={'permissions': [('special status', 'Can check all music')]},
        ),
    ]
