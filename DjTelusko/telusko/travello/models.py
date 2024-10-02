from django.db import models

# Create your models here.
# it is basically to connet to DB get desired data but here we are creating objects for now 

class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)