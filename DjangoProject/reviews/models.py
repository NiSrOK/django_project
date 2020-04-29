from django.db import models

class Data(models.Model):
    date = models.DateField()
    car = models.CharField(max_length = 100)
    number = models.IntegerField()
    comment = models.CharField(max_length = 100)
    rating = models.IntegerField()




