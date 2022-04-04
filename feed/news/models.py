from django.db import models


class NewsItem(models.Model):
    title = models.CharField(max_length=250)

    publish_date = models.DateTimeField(auto_now_add=True)

    body = models.TextField()

    # image = models.ImageField()
