from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100, blank=False)
    club = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return str(self.name)

class YearlyGoals(models.Model):
    class Meta:
        verbose_name = "YearlyGoals"
        verbose_name_plural = "YearlyGoals"
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    year=models.CharField(max_length=4)
    goals = models.IntegerField(default=0)

    def __str__(self):
        return "{} : {}".format(str(self.player), str(self.year))