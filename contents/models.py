from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=50, null=False)
    module = models.TextField()
    students = models.IntegerField()
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=False)
