from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProjectRight(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, default = None)
    project = models.CharField(max_length=40)
    CHOICES = (
        ('Choice1', 'Yes'),
        ('Choice2', 'No')

    )
    can_read = models.CharField(
        max_length=20,

        default='No',
    )
    can_write = models.CharField(
        max_length=20,

        default='No',
    )
    can_exec = models.CharField(
        max_length=20,

        default='No',
    )
    def __str__(self):
        return str(self.user) + '   ' +  str(self.project)