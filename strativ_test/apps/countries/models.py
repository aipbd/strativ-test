from django.db import models

# Create your models here.


class Country(models.Model):

    name = models.CharField(max_length=100)
    alpha_code2 = models.CharField(max_length=50)
    alpha_code3 = models.CharField(max_length=50, unique=True)
    capital = models.CharField(max_length=100)
    population = models.CharField(max_length=100)
    timezones = models.JSONField()
    flag = models.URLField(blank=True, null=True)
    languages = models.JSONField()
    neighbouring_countries = models.JSONField()

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
