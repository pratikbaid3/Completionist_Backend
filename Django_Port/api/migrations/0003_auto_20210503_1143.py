# Generated by Django 3.2 on 2021-05-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210503_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ps4Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.TextField(blank=True, null=True)),
                ('game_image_link', models.TextField(blank=True, null=True)),
                ('game_guide_url', models.TextField(blank=True, null=True)),
                ('gold', models.TextField(blank=True, db_column='GOLD', null=True)),
                ('silver', models.TextField(blank=True, db_column='SILVER', null=True)),
                ('bronze', models.TextField(blank=True, db_column='BRONZE', null=True)),
                ('platinum', models.TextField(blank=True, db_column='PLATINUM', null=True)),
            ],
            options={
                'db_table': 'PS4_Games',
            },
        ),
        migrations.AlterModelOptions(
            name='ps4gamesguide',
            options={},
        ),
        migrations.AlterField(
            model_name='ps4gamesguide',
            name='game_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ps4gamesguide',
            name='trophy_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ps4gamesguide',
            name='trophy_guide',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ps4gamesguide',
            name='trophy_image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ps4gamesguide',
            name='trophy_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ps4gamesguide',
            name='trophy_type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ps4gamesguide',
            name='youtube_link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterModelTable(
            name='ps4gamesguide',
            table='PS4_Games_Guide',
        ),
        migrations.DeleteModel(
            name='PS4Game',
        ),
    ]
