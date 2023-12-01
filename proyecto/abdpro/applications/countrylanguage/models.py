from django.db import models

# Create your models here.
class countrylanguage(models.Model):
    CountryCode = models.CharField('Code' , max_length=3 , unique=True)
    Language = models.CharField('Name' , max_length=30, primary_key=True)
    IsOfficial = models.IntegerField('IsOfficial' , max_length=5)
    Percentage = models.IntegerField('Percentage' , max_length=4)
    SecondLanguage = models.CharField('SecondLanguage' , max_length=20)
    RankingPosition = models.IntegerField('RankingPosition' , max_length=5)
    
    class Meta:
            verbose_name = 'Nombre countrylanguage'
            verbose_name_plural = 'Nombres countrylanguages'
            ordering = ['nombrecountrylanguage']
            unique_together = ('nombrecountrylanguage', 'siglacountrylanguage')
    def __str__(self):
        return self.nombrecountrylanguage + ' - ' + self.siglacountrylanguage + str(self.id)
    
