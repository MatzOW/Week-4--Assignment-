from django.db import models

# Create your models here.
class student(models.Model):
    firstname=models.CharField(max_length=15)
    lastname=models.CharField(max_length=15)
    student_id=models.IntegerField()

    def __str__(self):                                                 # There is double underscore both sides
        return self.firstname
