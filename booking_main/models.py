from django.db import models

class Rooms(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField(null=False)
    projector = models.BooleanField(null=False)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Reservations(models.Model):
    date = models.DateField()
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=False, related_name='reservations')
    comment = models.TextField(null=True)
    
    def __str__(self):
        return self.date
    
    class Meta:
        unique_together = ('date', 'room')
