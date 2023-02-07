from django.core.exceptions import ValidationError
from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def clean(self):
        if len(self.task) < 4:
            raise ValidationError("Task must be at least 4 characters long")

    def __str__(self):
        return self.task