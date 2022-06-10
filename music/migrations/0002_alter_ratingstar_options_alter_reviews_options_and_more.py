# Generated by Django 4.0.4 on 2022-05-26 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['value'], 'verbose_name': 'Звезда рейтинга', 'verbose_name_plural': 'Звезды рейтинга'},
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'ordering': ['-id'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='movie',
            new_name='music',
        ),
    ]
