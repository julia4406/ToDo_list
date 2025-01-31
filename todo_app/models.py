from django.db import models

class Task(models.Model):
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    tag = models.ManyToManyField("Tag", related_name="tags")


class Tag(models.Model):
    name = models.CharField(max_length=255)
