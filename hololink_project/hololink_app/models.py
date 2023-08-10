from django.db import models


class Question(models.Model):
    name = models.CharField(max_length=30)
    youtube_base_url = models.URLField()
    start_time = models.PositiveIntegerField()
    sentence = models.TextField()