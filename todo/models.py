from django.db import models
import datetime
from django.utils.timezone import now

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    date_due = models.DateTimeField(default=now, editable=False)

    def _str_(self):
        return self.title