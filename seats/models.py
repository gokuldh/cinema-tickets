from django.db import models
from datetime import datetime

# Create your models here.

class Seats(models.Model):
    seat_no = models.PositiveSmallIntegerField(blank=False, null=False, unique=True)
    row_no = models.PositiveSmallIntegerField(blank=False, null=False)
    seat_name = models.CharField(max_length=3, unique=True)
    booked_by = models.CharField(max_length=200, blank=True)
    ip= models.CharField(max_length=39, unique=True, blank=True)
    def __str__(self):
        return self.seat_name
    class Meta:
        verbose_name_plural= "Seats"

    