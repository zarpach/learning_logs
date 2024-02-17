from django.db import models


class Task(models.Model):
    status = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
