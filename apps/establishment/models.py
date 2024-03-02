from django.db import models

class Establishment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    opening_hours = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    