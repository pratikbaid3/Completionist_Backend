from django.db import models


# Create your models here.
class PS4Game(models.Model):
    class Meta:
        verbose_name = 'PS4 Game'
        verbose_name_plural = 'PS4 Games'
        ordering = ['id']

    game_name = models.CharField(max_length=500)
    game_image_link = models.CharField(max_length=500)
    game_guide_url = models.CharField(max_length=500)
    GOLD = models.IntegerField()
    SILVER = models.IntegerField()
    BRONZE = models.IntegerField()
    PLATINUM = models.IntegerField()

    def __str__(self):
        return self.game_name


class PS4GamesGuide(models.Model):
    class Meta:
        verbose_name = 'PS4 Guide'
        verbose_name_plural = 'PS4 Guides'
        ordering = ['id']
    game_name = models.ForeignKey(PS4Game, on_delete=models.DO_NOTHING)
    trophy_name = models.CharField(max_length=500)
    trophy_image = models.CharField(max_length=500)
    trophy_type = models.CharField(max_length=500)
    trophy_description = models.CharField(max_length=500)
    trophy_guide = models.CharField(max_length=500)
    youtube_link = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.trophy_name
