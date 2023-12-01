from django.db import models

# Create your models here.
class country(models.Model):
    Code = models.CharField('Code' , max_length=3 , primary_key=True)
    Name = models.CharField('Name' , max_length=52)
    Continent = models.CharField('Continent' , max_length=15)
    Region = models.CharField('Region' , max_length=26)
    SurfaceArea = models.IntegerField('SurfaceArea' , max_length=10)
    IndepYear = models.IntegerField('IndepYear' , max_length=10)
    Population = models.IntegerField('Population' , max_length=10)
    LifeExpentancy = models.IntegerField('LifeExpentancy' , max_length=3)  
    GNP = models.IntegerField('GNP' , max_length=10)
    GNPOld = models.IntegerField('GNPOld' , max_length=10)
    LocalName = models.CharField('LocalName' , max_length=45)
    GovernmentForm = models.CharField('GovernmentForm' , max_length=45)
    HeadOfState = models.CharField('HeadOfState' , max_length=60)
    Capital = models.CharField('Capital' , max_length=20)
    Code2 = models.CharField('Code2' , max_length=2)
    NumberCities = models.IntegerField('NumberCities' , max_length=20)
    MayorsNumber = models.IntegerField('MayorsNumber' , max_length=10)
    
    class Meta:
            verbose_name = 'Nombre country'
            verbose_name_plural = 'Nombres countrys'
            ordering = ['nombrecountry']
            unique_together = ('nombrecountry', 'siglacountry')
    def __str__(self):
        return self.nombrecountry + ' - ' + self.siglacountry + str(self.id)
    