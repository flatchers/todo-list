from django.db import models


class Task(models.Model):
    content = models.TextField(null=False, blank=False)
    datetime = models.DateField()
    deadline = models.DateField(null=True)
    is_done = models.BooleanField()
    tags = models.CharField(max_length=255)


class Tag(models.Model):
    theme = models.CharField(max_length=255)
