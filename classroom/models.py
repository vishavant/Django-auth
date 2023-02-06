from django.db import models

# Create your models here.


class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ClassRoom(models.Model):
    name = models.CharField(max_length=150)
    short_description = models.CharField(max_length=250, blank=True)
    capacity = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    