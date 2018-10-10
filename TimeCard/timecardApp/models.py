from django.db import models


class Timesheet(models.Model):
    name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    dateOfWork = models.DateField()
    dateOfEntry = models.DateField()


def __str__(self):
    return self.name



