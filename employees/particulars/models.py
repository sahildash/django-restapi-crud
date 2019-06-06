from django.db import models

class Particulars(models.Model):
    firstname = models.CharField(max_length=50)
    lastname  = models.CharField(max_length=50)
    companyname= models.CharField(max_length=50)
    state= models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    age= models.IntegerField()
    zip= models.IntegerField()

    web= models.CharField(max_length=50)

    def __str__(self):
        return self.firstname
