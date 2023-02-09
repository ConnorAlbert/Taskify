from django.core.exceptions import ValidationError
from django.db import models

class Todo(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    task = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='Low')
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.task

    class Meta:
        ordering = ['order']