from django.db import models

STATUS = (
    ('done', 'Выполнено'),
    ('not done', 'Не выполнено'),
)


class Task(models.Model):
    status = models.CharField(max_length=255, choices=STATUS)
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
