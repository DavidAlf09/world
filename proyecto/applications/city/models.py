from django.db import models

# Create your models here.
class city(models.Model):
    ID = models.IntegerField('ID' , max_length=20, primary_key=True )
    name = models.CharField('name' , max_length=35)
    CountryCode = models.CharField('CountryCode' , max_length=3 , unique=True)
    District = models.CharField('District' , max_length=20)
    Population = models.CharField('Population' , max_length=35)
    PostalCode = models.IntegerField('PostalCode' , max_length=10)
    Neighborhoods = models.IntegerField('Neighborhoods' , max_length=10)
    
    class Meta:
            verbose_name = 'Nombre city'
            verbose_name_plural = 'Nombres citys'
            ordering = ['nombrecity']
            unique_together = ('nombrecity', 'siglacity')
    def __str__(self):
        return self.nombrecity + ' - ' + self.siglacity + str(self.id)
    