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

    def clean(self):
        if len(self.task) < 4:
            raise ValidationError("Task must be at least 4 characters long")

    def __str__(self):
        return self.task