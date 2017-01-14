from django.db import models


# Create your models here.
class Player(models.Model):
    playerID = models.CharField(max_length=50)
    positionName = models.CharField(max_length=50)
    playerfirstName = models.CharField(max_length=100)
    playerlastName = models.CharField(max_length=100)
    teamAbbreviation = models.CharField(max_length=50)
    teamCity = models.CharField(max_length=100)
    teamName = models.CharField(max_length=100)

    def __str__(self):
        return self.playerlastName, self.playerfirstName

class PlayerRawStats(models.Model):
    playerStatKey = models.CharField(max_length=100)
    dateStat = models.DateField('date of stat')
    playerID = models.CharField(max_length=50)
    statisticType = models.CharField(max_length=100)
    statAmt = models.FloatField(default=0)

    def __str__(self):
        return self.playerStatKey

class PergameTotals(models.Model):
    pergameTotalKey = models.CharField(max_length=100)
    dateStat = models.DateField('date of stat')
    playerID = models.CharField(max_length=50)
    statAmt = models.FloatField(default=0)

    def __str__(self):
        return self.pergameTotalKey

