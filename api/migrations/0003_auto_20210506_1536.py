# Generated by Django 3.2.2 on 2021-05-06 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210504_1456'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ps4games',
            options={'ordering': ['game_name'], 'verbose_name': 'PS4 Game', 'verbose_name_plural': 'PS4 Games'},
        ),
        migrations.AlterModelOptions(
            name='ps4gamesguide',
            options={'ordering': ['game_name'], 'verbose_name': 'PS4 Game Guide', 'verbose_name_plural': 'PS4 Game Guides'},
        ),
    ]
