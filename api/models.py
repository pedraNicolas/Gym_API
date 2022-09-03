from sys import maxsize
from django.db import models
from .choices import shifts
from datetime import date
# Create your models here.


class Activity(models.Model):
    activity_id = models.BigAutoField(
        auto_created=True, primary_key=True, null=False)
    activity_name = models.CharField(max_length=50)
    start_time = models.TimeField(null=False)
    finish_time = models.TimeField(null=False)
    shift_duration = models.TimeField(null=False)
    activity_on_monday = models.BooleanField(null=False, default=False)
    activity_on_tuesday = models.BooleanField(null=False, default=False)
    activity_on_wednesday = models.BooleanField(null=False, default=False)
    activity_on_thursday = models.BooleanField(null=False, default=False)
    activity_on_friday = models.BooleanField(null=False, default=False)
    activity_on_saturday = models.BooleanField(null=False, default=False)

    def __str__(self):
        return '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}'.format(
            self.activity_name, self.start_time, self.finish_time, self.shift_duration, self.activity_on_monday, self.activity_on_tuesday, self.activity_on_wednesday, self.activity_on_thursday, self.activity_on_friday, self.activity_on_saturday)


class Shift(models.Model):
    shift_name = models.CharField(max_length=5, choices=shifts)
    shift_id = models.BigAutoField(
        auto_created=True, primary_key=True, null=False)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    shift_date = models.DateField(null=False, default=date.today)

    class Meta:
        verbose_name = 'Shift'
        verbose_name_plural = 'Shifts'
        db_table = 'shifts'
        ordering = ['shift_name']
    def __str__(self):
        return '{0},{1},{2}'.format(
            self.activity,self.shift_name,self.shift_date)
