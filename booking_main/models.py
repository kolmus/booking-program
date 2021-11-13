from django.db import models

# Create your models here.
class Rooms(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField(null=False)
    projector = models.BooleanField(null=False)
    
    # def __str__(self):
    #     return self.name


