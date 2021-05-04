from django.db import models


class Ps4Games(models.Model):
    class Meta:
        verbose_name = 'PS4 Game'
        verbose_name_plural = 'PS4 Games'
        db_table = 'PS4_Games'
        ordering = ['game_name']

    game_name = models.TextField(primary_key=True)
    game_image_link = models.TextField(blank=True, null=True)
    game_guide_url = models.TextField(blank=True, null=True)
    gold = models.TextField(db_column='GOLD', blank=True, null=True)
    silver = models.TextField(db_column='SILVER', blank=True, null=True)
    bronze = models.TextField(db_column='BRONZE', blank=True, null=True)
    platinum = models.TextField(db_column='PLATINUM', blank=True, null=True)

    def __str__(self):
        return self.game_name


class Ps4GamesGuide(models.Model):
    class Meta:
        verbose_name = 'PS4 Game Guide'
        verbose_name_plural = 'PS4 Game Guides'
        db_table = 'PS4_Games_Guide'
        ordering =['game_name']

    game_name = models.TextField(blank=True, null=True)
    trophy_name = models.TextField(primary_key=True)
    trophy_image = models.TextField(blank=True, null=True)
    trophy_type = models.TextField(blank=True, null=True)
    trophy_description = models.TextField(blank=True, null=True)
    trophy_guide = models.TextField(blank=True, null=True)
    youtube_link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.game_name
