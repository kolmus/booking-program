from django.db import models

class Rooms(models.Model):
    """Model of table Rooms. Represents base of all rooms 

    Args:
        models: from Django

    Returns:
        __str__: name of room
    """    
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField(null=False)
    projector = models.BooleanField(null=False)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Reservations(models.Model):
    """Model of reservation dates for each room

    Args:
        models ([type]): [description]

    Returns:
        __str__: date of reservation
    """    
    date = models.DateField()
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=False, related_name='reservations')
    comment = models.TextField(null=True)
    
    def __str__(self):
        return self.date
    
    class Meta:
        unique_together = ('date', 'room')
